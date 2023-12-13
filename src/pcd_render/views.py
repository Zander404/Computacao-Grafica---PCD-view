import os
from django.shortcuts import render
from django.conf import settings

def get_file_count(folder_path):
    file_count = sum(len(files) for _, _, files in os.walk(folder_path))
    return file_count

def index(request):
    folder_path = os.path.join(settings.BASE_DIR, 'staticfiles/images/andrew9/ply')
    images_path = "images/andrew9/ply/frame"
    # Verify that the folder exists before trying to get the file count
    if os.path.exists(folder_path):
        frames = get_file_count(folder_path)
        return render(request, "index1.html", {'frames': frames, 'file_path': str(images_path)})
 

def point_cloud1(request):
    path = "images/david9/ply"
    images_path = f"{path}/frame"
    folder_path = os.path.join(settings.BASE_DIR, f'staticfiles/{path}')
    # Verify that the folder exists before trying to get the file count
    if os.path.exists(folder_path):
        frames = get_file_count(folder_path)
        return render(request, "index1.html", {'frames': frames, 'file_path': str(images_path)})

def point_cloud2(request):
    path = "images/sarah9/ply"
    images_path = f"{path}/frame"
    folder_path = os.path.join(settings.BASE_DIR, f'staticfiles/{path}')
    # Verify that the folder exists before trying to get the file count
    if os.path.exists(folder_path):
        frames = get_file_count(folder_path)
        return render(request, "index1.html", {'frames': frames, 'file_path': str(images_path)})
