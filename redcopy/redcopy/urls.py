from django.contrib import admin
from django.urls import path, include, re_path
from shorturlsapp import views as shortviews
from blogapp import views as blogviews

urlpatterns = [
    path('accounts/', include('accounts.urls')),
    # path('accounts/login/', templates.LoginView.as_view(template_name='myapp/login.html')),
    path('blog/', include('blogapp.urls')),
    path('/', include('shorturlsapp.urls')),
    path('', include('shorturlsapp.urls')),
    path('admin/', admin.site.urls),
    path('short/', include('shorturlsapp.urls')),
    re_path(r'(?P<rnd_string>\w{5})$', shortviews.shorturl),

]
