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

# Create your views here.
# class HomeView(View):
BaseURL = "http://localhost:8000"
uploaded_image = ''
def Home(request):
    form = StudentForm()
    uploaded_image = BaseURL + "/media/uploads/empty.png"
    return render(request, 'home.html', {'form' : form, 'imageurl' : uploaded_image})
    # template = loader.get_template('home.html')
    # return HttpResponse(template.render())

@csrf_exempt
def upload(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        uploaded_image = BaseURL + "/media/uploads/" + str(request.FILES['path'])

        if form.is_valid():
            form.save()
            # return redirect('success')
            return render(request, 'home.html', {'form' : form, 'imageurl' : uploaded_image})
    # print(request.POST['url'])
    # # print(request.POST['file'])
    # # saveimage(request.POST['url'])
    # template = loader.get_template('home.html')
    # return HttpResponse(template.render())

def Save(request):
    form = StudentForm()
    if request.POST['type'] == 'Custom':
        saveimage(type="Custom", w=request.POST['width'], h=request.POST['height'])
    else :
        saveimage(type=request.POST['type'])
    return render(request, 'home.html', {'form' : form, 'imageurl' : uploaded_image})

def saveimage(self, **kwargs):
    if kwargs['type'] == "Custom":
        image = Image.open(uploaded_image)
        new_image = image.resize((kwargs['w'], kwargs['h']))
        new_image.save(self.BaseURL + '/resize/myimage_500.jpg')
    # absolute_path = os.path.dirname(os.path.abspath(__file__))
    # filepath = absolute_path + "/templates/example.jpg"
    # image = Image.open(filepath)
    # new_image = image.resize((500, 500))
    # new_image.save(absolute_path + '/myimage_500.jpg')


# from django.http import HttpResponse
# from django.shortcuts import render, redirect
# from .form import *


# def avatarView(request):

#     if request.method == 'POST':
#         print(request.POST)
#         print(request.FILES)
#         form = StudentForm(request.POST, request.FILES)

#         if form.is_valid():
#             form.save()
#             return redirect('success')
#     else:
#         form = StudentForm()
#     return render(request, 'studentform.html', {'form' : form})


# def uploadok(request):
#     return HttpResponse(' upload successful')