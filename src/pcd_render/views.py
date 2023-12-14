import os
from pdb import post_mortem
from django.shortcuts import render,  redirect
from django.conf import settings
from django.http import HttpResponseRedirect
from .form import Form


def get_file_count(folder_path):
    file_count = sum(len(files) for _, _, files in os.walk(folder_path))
    return file_count


def index(request):
    return render(request, 'home.html')

def point_cloud1(request):
    path = "images/david9/ply"
    images_path = f"{path}/frame"
    folder_path = os.path.join(settings.BASE_DIR, f'staticfiles/{path}')
    # Verify that the folder exists before trying to get the file count
    if os.path.exists(folder_path):
        frames = get_file_count(folder_path)
        return render(request, "index.html", {'frames': frames, 'file_path': str(images_path)})

def point_cloud2(request):
    path = "images/sarah9/ply"
    images_path = f"{path}/frame"
    folder_path = os.path.join(settings.BASE_DIR, f'staticfiles/{path}')
    # Verify that the folder exists before trying to get the file count
    if os.path.exists(folder_path):
        frames = get_file_count(folder_path)
        return render(request, "index1.html", {'frames': frames, 'file_path': str(images_path)})

def point_cloud3(request):
    path = "images/andrew9/ply"
    images_path = f"{path}/frame"
    folder_path = os.path.join(settings.BASE_DIR, f'staticfiles/{path}')
    # Verify that the folder exists before trying to get the file count
    if os.path.exists(folder_path):
        frames = get_file_count(folder_path)
        return render(request, "index1.html", {'frames': frames, 'file_path': str(images_path)})



def form(request):
    if request.method == 'POST':
        form = Form(request.POST)
        if form.is_valid():
            form.save()

            # Redirect to a success page or do something else
            return HttpResponseRedirect('/thank_you/')         
    else:
        form = Form()
    return render(request, "form.html", {'form': form })