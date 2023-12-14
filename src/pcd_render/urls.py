from django.urls import path
from pcd_render import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', view=views.index),
    path('image1', view=views.point_cloud1, name="image1"),
    path('image2', view=views.point_cloud2, name='image2'),
    path('image3', view=views.point_cloud3, name='image3'),
    path('form', view=views.form, name='form'),
    path('thank_you', view=views.index, name='thank_you'),

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)