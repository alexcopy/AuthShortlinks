from django.urls import path, include, re_path
from . import views

urlpatterns = [
    path('', views.index, name='short_index'),
    path('redirect/', views.short_url, name='redirect'),
    re_path(r'redirect/(?P<rnd_string>\w{5,5})/$', views.short_url, name='redirect'),
    path('delete/<url_id>/', views.delete_shorturl, name='delete_post'),
]
