from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# from .models import Member
from itertools import chain
from django.views.decorators.csrf import csrf_exempt
from PIL import Image
import os
from django.views import View
from .form import *
from django.conf import settings

# Create your views here.
# class HomeView(View):
BaseURL = "http://localhost:8000"
uploaded_image = ''
url = ''
def Home(request):
    form = StudentForm()
    global uploaded_image
    uploaded_image = BaseURL + "/media/uploads/empty.png"
    return render(request, 'home.html', {'form' : form, 'imageurl' : uploaded_image})

@csrf_exempt
def upload(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        global uploaded_image
        uploaded_image = "/uploads/" + str(request.FILES['path'])
        global url
        url = BaseURL + "/media/uploads/" + str(request.FILES['path'])

        if form.is_valid():
            form.save()
            # return redirect('success')
            return render(request, 'home.html', {'form' : form, 'imageurl' : url})

@csrf_exempt
def Save(request):
    file_path = os.path.join(settings.MEDIA_ROOT,'uploads')
    file = request.POST['name'].split(".")
    resize_path = os.path.join(settings.MEDIA_ROOT, 'resize')
    save_path = os.path.join(resize_path, file[0])
    os.mkdir(save_path)
    thumbnail_path = os.path.join(save_path, 'thumbnail.' + file[1])
    origin_path = os.path.join(save_path, 'origin.' + file[1])
    middle_path = os.path.join(save_path, 'middle.' + file[1])
    big_path = os.path.join(save_path, 'big.' + file[1])
    
    form = StudentForm()
    file_origin = os.path.join(file_path, request.POST['name'])
    image = Image.open(file_origin)
    origin = image.save(origin_path)
    new_thumbnail = image.resize((90,90))
    new_middle = image.resize((150,150))
    new_big = image.resize((1000,600))

    new_thumbnail.save(thumbnail_path)
    new_middle.save(middle_path)
    new_big.save(big_path)
    
    return render(request, 'home.html', {'form' : form, 'imageurl' : url})
