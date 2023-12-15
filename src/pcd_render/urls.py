from django.urls import path
from pcd_render import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', view=views.index),
    path('video1', view=views.point_cloud_video1, name="video1"),
    path('video2', view=views.point_cloud_video2, name='video2'),
    path('video3', view=views.point_cloud_video3, name='video3'),
    path('image1', view=views.point_cloud_image1, name="image1"),
    path('image2', view=views.point_cloud_image2, name='image2'),
    path('image3', view=views.point_cloud_image3, name='image3'),
    path('form', view=views.form, name='form'),
    

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)