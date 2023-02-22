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
    try:
        os.mkdir(save_path)
    except:
        pass
    
    form = StudentForm()
    file_origin = os.path.join(file_path, request.POST['name'])
    image = Image.open(file_origin)
    
    webp_path = os.path.join(save_path, 'webp')
    
    try:
        os.mkdir(webp_path)
        webp_thumbnail_path = os.path.join(webp_path, 'thumbnail.webp')
        webp_origin_path = os.path.join(webp_path, 'origin.webp')
        webp_middle_path = os.path.join(webp_path, 'middle.webp')
        webp_big_path = os.path.join(webp_path, 'big.webp')
        
        webp_origin = image.save(webp_origin_path)
        webp_new_thumbnail = image.resize((90,90))
        webp_new_middle = image.resize((150,150))
        webp_new_big = image.resize((1000,600))
        webp_new_thumbnail.save(webp_thumbnail_path)
        webp_new_middle.save(webp_middle_path)
        webp_new_big.save(webp_big_path)
    except:
        pass
    
    
    if request.POST['type'] == "logo":
        png_path = os.path.join(save_path, 'png')
        try:
            os.mkdir(png_path)
            png_thumbnail_path = os.path.join(png_path, 'thumbnail.png')
            png_origin_path = os.path.join(png_path, 'origin.png')
            png_middle_path = os.path.join(png_path, 'middle.png')
            png_big_path = os.path.join(png_path, 'big.png')
            png_new_thumbnail = image.resize((90,90))
            png_new_middle = image.resize((150,150))
            png_new_big = image.resize((1000,600))
            
            png_origin = image.save(png_origin_path)
            png_new_thumbnail.save(png_thumbnail_path)
            png_new_middle.save(png_middle_path)
            png_new_big.save(png_big_path)
        except:
            pass
    else :
        jpg_path = os.path.join(save_path, 'jpg')
        try:
            os.mkdir(jpg_path)
            jpg_thumbnail_path = os.path.join(jpg_path, 'thumbnail.jpg')
            jpg_origin_path = os.path.join(jpg_path, 'origin.jpg')
            jpg_middle_path = os.path.join(jpg_path, 'middle.jpg')
            jpg_big_path = os.path.join(jpg_path, 'big.jpg')
            jpg_new_thumbnail = image.resize((90,90))
            jpg_new_middle = image.resize((150,150))
            jpg_new_big = image.resize((1000,600))
            
            jpg_origin = image.save(jpg_origin_path)
            jpg_new_thumbnail.save(jpg_thumbnail_path)
            jpg_new_middle.save(jpg_middle_path)
            jpg_new_big.save(jpg_big_path)
        except:
            pass
        
    
    return render(request, 'home.html', {'form' : form, 'imageurl' : url})
