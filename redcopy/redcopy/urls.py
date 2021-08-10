from django.contrib import admin
from django.urls import path, include, re_path
from shorturlsapp import views

urlpatterns = [
    path('accounts/', include('accounts.urls')),
    # path('accounts/login/', templates.LoginView.as_view(template_name='myapp/login.html')),
    path('short/', include('shorturlsapp.urls')),
    path('/', include('shorturlsapp.urls')),
    path('', include('shorturlsapp.urls')),
    path('admin/', admin.site.urls),
    path('<str:rnd_string>/', views.shorturl),

]
