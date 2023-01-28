from django.shortcuts import render,redirect
from .forms import *

def form(request):
    if request.method == 'POST':
        form = Form(request.POST)
        if form.is_valid:
            form.save()
            return redirect('index.html')
    else:
        form = Form()
    return render(request,'index.html',{'form':form})
