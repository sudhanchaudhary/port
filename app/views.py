from django.shortcuts import render
from .models import Message
from django.contrib import messages
# Create your views here.
def home(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        msg=request.POST.get('msg')        
        Message.objects.create(name=name,email=email,message=msg)
        messages.success(request,"Message Sent Successfully.")
            
    return render(request,'home.html')

