from django.urls import include, path
from pcd_render import views

urlpatterns = [
    path('teste', view=views.index)

]