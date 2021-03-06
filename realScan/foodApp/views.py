from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Ingredient
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.contrib import messages

def main(request):
    template_name = 'gender.html'
    return render(request, 'gender.html')

def form(request):
    template_name = 'form.html'
    return render(request, 'form.html')

def form1(request):
    template_name = 'form1.html'
    return render(request, 'form1.html')

def calculate_man(request):
    if request.method == "POST":
        try:
            post = Ingredient.objects.get(barcode=request.POST['barcode_num'])
            return render(request, 'main.html', {"post" : post})
        except:
            messages.info(request, "등록되지 않은 바코드입니다.")
    else:
        pass
    return render(request, 'form1.html')   

def calculate(request):
    
    if request.method == "POST":
        try:
            post = Ingredient.objects.get(barcode=request.POST['barcode_num'])
            return render(request, 'main.html', {"post" : post})
        except:
            messages.info(request, "등록되지 않은 바코드입니다.")
            
    else:
        pass
    return render(request, 'form.html')

def detail1(request, detail_id):
    detail_obj = get_object_or_404(Ingredient, pk = detail_id)
    return render(request, 'detail1.html', {"detail_key":detail_obj})

def detail2(request, detail_id):
    detail_obj = get_object_or_404(Ingredient, pk = detail_id)
    return render(request, 'detail2.html', {"detail_key":detail_obj})

def detail3(request, detail_id):
    detail_obj = get_object_or_404(Ingredient, pk = detail_id)
    return render(request, 'detail3.html', {"detail_key":detail_obj})

def detail4(request, detail_id):
    detail_obj = get_object_or_404(Ingredient, pk = detail_id)
    return render(request, 'detail4.html', {"detail_key":detail_obj})

def detail5(request, detail_id):
    detail_obj = get_object_or_404(Ingredient, pk = detail_id)
    return render(request, 'detail5.html', {"detail_key":detail_obj})

def detail6(request, detail_id):
    detail_obj = get_object_or_404(Ingredient, pk = detail_id)
    return render(request, 'detail6.html', {"detail_key":detail_obj})

def detailman1(request, detail_id):
    detail_obj = get_object_or_404(Ingredient, pk = detail_id)
    return render(request, 'detail_man1.html', {"detail_key":detail_obj})

def detailman2(request, detail_id):
    detail_obj = get_object_or_404(Ingredient, pk = detail_id)
    return render(request, 'detail_man2.html', {"detail_key":detail_obj})

def detailman3(request, detail_id):
    detail_obj = get_object_or_404(Ingredient, pk = detail_id)
    return render(request, 'detail_man3.html', {"detail_key":detail_obj})

def detailman4(request, detail_id):
    detail_obj = get_object_or_404(Ingredient, pk = detail_id)
    return render(request, 'detail_man4.html', {"detail_key":detail_obj})

def detailman5(request, detail_id):
    detail_obj = get_object_or_404(Ingredient, pk = detail_id)
    return render(request, 'detail_man5.html', {"detail_key":detail_obj})

def detailman6(request, detail_id):
    detail_obj = get_object_or_404(Ingredient, pk = detail_id)
    return render(request, 'detail_man6.html', {"detail_key":detail_obj})