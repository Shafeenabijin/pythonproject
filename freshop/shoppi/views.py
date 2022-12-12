from django.http import HttpResponse
from django.shortcuts import render,redirect
from . models import place
from .forms import ModeForm

# Create your views here.
def fun(request):
    obj=place.objects.all()
    return render(request,"index.html",{'results':obj})


def edit(request,place_id):
    obj1=place.objects.get(id=place_id)
    return render(request,"edit.html",{'resultt':obj1})
def add_product(request):
    if request.method=='POST':
        name=request.POST.get('name')
        price=request.POST.get('price')

        img=request.FILES['img']
        p=place(name=name,price=price,img=img)
        p.save()
        print("product added")
    return render(request,"add_product.html")
def update(request,id):
    obj=place.objects.get(id=id)
    form=ModeForm(request.POST or None,request.FILES,instance=obj)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'ed.html',{'form':form,'obj':obj})
def delete(request,id):
    if request.method=='POST':
        obj=place.objects.get(id=id)
        obj.delete()
        return redirect('/')
    return render(request,'delete.html')





