from django.shortcuts import render,redirect
from .models import Message,Portfolio,TechCategory,Project
from django.contrib import messages
# Create your views here.
def home(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        msg=request.POST.get('msg')        
        Message.objects.create(name=name,email=email,message=msg)
        messages.success(request,"Message Sent Successfully.")
        return redirect('home')
    project=Project.objects.all()
    cate=TechCategory.objects.all()
    resume=Portfolio.objects.first()
    context={
        'resume':resume,
        'cate':cate,
        'project':project
    }
    return render(request,'home.html',context)

