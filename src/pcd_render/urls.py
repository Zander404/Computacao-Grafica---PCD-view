from django.urls import path
from pcd_render import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', view=views.index),
    path('1', view=views.point_cloud1),
    path('2', view=views.point_cloud2),
    path('form', view=views.form, name='form'),
    path('thank_you', view=views.index, name='thank_you'),

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)