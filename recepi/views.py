from django.shortcuts import render,redirect
from .models import *
# Create your views here.


def receipe(request):
    if request.method=="POST":
        data=request.POST
        name=data.get('name')
        descp=data.get('descp')
        img=request.FILES.get('img')
        Receipe.objects.create(
          name=name,
          descp=descp,
          img=img
        )
        return redirect('/receipe/')
    queryset=Receipe.objects.all()
    if request.GET.get('search'):
        queryset=queryset.filter(name__icontains=request.GET.get('search'))
        print(request.GET.get('search'))
    context={'receipe':queryset}
    
      
    return render(request,'receipe.html',context)

def updaterecp(request,id):
    q=Receipe.objects.get(id=id)
    if request.method=="POST":
        data=request.POST
        name=data.get('name')
        descp=data.get('descp')
        img=request.FILES.get('img')
        q.name=name
        q.descp=descp
        if img:
            q.img=img
        q.save()  
        return redirect('/receipe/')
        
           
    context={'receipe':q}
    return render(request,'update_recp.html',context)

def delete_recp(request,id):
    q=Receipe.objects.get(id=id)
    q.delete()
    return redirect('/receipe/')
