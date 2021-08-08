from django import forms
from django.contrib.auth import authenticate, get_user_model

User = get_user_model()


class UserLoginForm(forms.Form):
    username = forms.CharField(label='Email Address', max_length=50, widget=forms.TextInput
    (attrs={'class': 'input',
            'id': 'id_username'}))
    password = forms.CharField(max_length=50, widget=forms.PasswordInput(
        attrs={'class': 'input',
               'id': 'id_password'}))

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError('This user does not exist')
            if not user.check_password(password):
                raise forms.ValidationError('Incorrect Password')
            if not user.is_active:
                raise forms.ValidationError('This user is not active')
        return super(UserLoginForm, self).clean(*args, *kwargs)


class UserRegisterForm(forms.ModelForm):
    attrs={'class': 'input'}
    username = forms.CharField(label='Name', max_length=50, widget=forms.TextInput(attrs=attrs))
    email = forms.EmailField(label='Email', widget=forms.TextInput(attrs=attrs))
    email2 = forms.EmailField(label='Confirm Email',  widget=forms.TextInput(attrs=attrs))
    password = forms.CharField(widget=forms.PasswordInput(attrs=attrs))

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'email2',
            'password',
        ]


def clean_email(self, *args, **kwargs):
    email = self.cleaned_data.get('email')
    email2 = self.cleaned_data.get('email2')
    if email != email2:
        raise forms.ValidationError('emails must match')
    email_qs = User.objects.filter(email=email)
    if email_qs.exists():
        raise forms.ValidationError(
            'This email is already being used'
        )
    return super(UserRegisterForm, self.clean(*args, **kwargs))
