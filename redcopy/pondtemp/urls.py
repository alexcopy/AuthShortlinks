from django.template.defaulttags import url
from django.urls import path, include, re_path
from django.views.generic import RedirectView

from . import views

urlpatterns = [
    path('meters', views.meters, name='pondmeters'),
    path('cams',  views.cams, name='allcams'),
    path('allfiles/details/',  views.cams_harvest_details, name='camsdetailes'),
    # path('api',  views.cams_harvest_details, name='camsdetailes'),
    path(r'^api/(?P<path>.*)$', RedirectView.as_view(url='/pondtemp/%(path)s')),



    # path('', views.IndexPostsView.as_view(), name='indexblog'),
    # path('myposts', views.IndexPostsViewByUser.as_view(), name='myposts'),
    # path('add_post/', views.AddPostView.as_view(), name='addpost'),
    # # path('delete/<url_id>/', views.delete_shorturl, name='delete_post'),
    # path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_view'),
    # path('post/edit/<int:pk>/', views.UpdatePostView.as_view(), name='post_edit'),
    # path('post/<int:pk>/delete', views.DeletePostView.as_view(), name='post_delete'),
]
