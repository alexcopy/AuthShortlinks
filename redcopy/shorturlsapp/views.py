from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from django.forms.models import model_to_dict
from django.contrib.auth.decorators import login_required, permission_required

from . import forms
from .models import ShortLinks
from .services import short_url_service


@login_required
def index(request):
    posts = ShortLinks.objects.filter(user=request.user).order_by('-createdAt').all()
    context = {'form': {}, 'posts': posts, 'host': request.build_absolute_uri('/')[:-1]}
    if request.method == 'POST':
        try:
            form = forms.PostForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                rnd_string = short_url_service.rnd_string(5, 5)
                post.rnd_key = rnd_string
                post.user = request.user
                post.save()
                return redirect('redirect', rnd_string)
            else:
                context['form'] = form

                return render(request, 'shorturlsapp/index.html', context)
        except ValidationError as er:
            raise ValidationError(er.message)
    else:
        context['form'] = forms.PostForm()
    return render(request, 'shorturlsapp/index.html', context)


@login_required
def short_url(request, rnd_string=''):
    if len(rnd_string) < 4:
        return redirect('short_index')
    context = {'host': request.build_absolute_uri('/')[:-1], 'rnd_key': rnd_string}
    return render(request, 'shorturlsapp/redirect.html', context)


@login_required
def delete_shorturl(request, url_id):
    # check if sh_url belongs to user
    sh_url = ShortLinks.objects.get(id=url_id)
    if sh_url.user == request.user:
        sh_url.delete()
    return redirect('short_index')


def shorturl(request, rnd_string):
    if not len(rnd_string) == 5 or (not request.method == 'GET'):
        return redirect('shorturlsapp/404.html')
    record = ShortLinks.objects.filter(rnd_key=rnd_string)
    if not record.exists():
        return render(request, 'shorturlsapp/404.html')
    record = record.get()
    record.redirect_count += 1
    record.save()
    return redirect(record.origin_url)
