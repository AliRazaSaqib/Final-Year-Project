from django.shortcuts import render

from django.shortcuts import render, redirect
from check import detect
import os
from django.contrib import messages
from check import accuracy_check
# from django.http import HttpResponseRedirect, HttpResponse
from .forms import HotelForm
from .models import Hotel

package_dir = os.path.dirname(os.path.abspath(__file__))
# print(package_dir)
dir = str(package_dir)
dir = dir.replace('\\', '//')
file = dir[:-5]

global Path
Path = "http://127.0.0.1:8887/templates/images/forPreview.png"
# global statement
# statement = "Button is clicked"


def home(request):
    # if request.POST.get('second_click'):
    if request.method == "POST":
        form = HotelForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            obj = form.instance
            return render(request, 'home.html', {'obj': obj})
    else:
        form = HotelForm()
    return render(request, 'home.html', {'form': form})


def process(request):
    if request.method == "POST":
        print(12)
        value = request.POST['hotel_Main_Img']
        print(13)
        value2 = request.POST['get_block_size']
        print(value2)
        value3 = int(value2)
        print(value3)
        print(value)
        file = dir[:-5] + "templates//images//" + value
        print(file)
        # global Path
        image_name = detect.detect(file,
                                   dir[:-5] + "//templates//images//result//",
                                   value3)
        global Path
        Path = "http://127.0.0.1:8887/templates/images/result/" + image_name
    return render(request, 'process.html')


def help(request):
    return render(request, 'help.html')  # It will render the help module


def delete(request, id):
    obj = Hotel.objects.get(id=id)
    obj.delete()
    return redirect('/ImagePreview')


def ImagePreview(request):
    get_img = Hotel.objects.all()
    return render(request, 'history.html', {'fetch_images': get_img})


def edit(request, id):
    get_img = Hotel.objects.get(id=id)
    return render(request, 'edit.html', {'get_img': get_img})


def update(request, id):
    get_img = Hotel.objects.get(id=id)
    form = HotelForm(data=request.POST, files=request.FILES, instance=get_img)
    form.save()
    obj = form.instance
    return render(request, 'edit.html', {'obj': obj})


# def search(request):
#     # if 'q' in request.GET:
#     #     q = request.GET['q']
#     #     posts = Hotel.objects.filter(name__icontains=q)
#     # else:
#     #     posts = Hotel.objects.all()
#     given_name = request.get['q']
#     get_img = Hotel.objects.filter(name=given_name)
#     return render(request, 'history.html', {'get_img': get_img})


def final(request):
    print(Path)
    get_pt = Path
    return render(request, 'final.html', {'get_pt': get_pt})  # It will render the finale reuslt module


def developers(request):
    return render(request, 'developers.html',)


global accuracy1
global single_accuracy1
accuracy1 = 0.0
single_accuracy1 = 0.0


def accuracy(request, accuracy1=0.0, single_accuracy1=0.0):
    context = {}
    data = request.POST.get('mask1', None)
    context['data'] = single_accuracy1
    context['data1'] = accuracy1

    # avg_accuracy = avg_accuracy1
    # single_accuracy = single_accuracy1
    # single_accuracy = 0.0
    if request.POST.get('mask1'):
        sample=request.POST['sample']
        system=request.POST['system']
        system=file+"templates//images//result//"+system
        sample=file+"templates//images//Sample_masks//"+sample
        print("first button is clicked", system, sample)
        single_accuracy1=accuracy_check.check(sample,system)*100


    if request.POST.get('maks2'):
        accuracy1 = accuracy_check.getfolder() * 100
        print("second button is clicked")
    context['data'] = single_accuracy1
    context['data1'] = accuracy1
    return render(request, 'Accuracy.html', context)

# def development(request):
#     return render(request,'developers.html')