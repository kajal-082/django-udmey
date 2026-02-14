from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import logout as auth_logout
from django.contrib import messages

from .forms import RegisterForm
# Create your views here.
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
           form.save()
           username = form.cleaned_data.get('username')
           messages.success(request,f'welcome {username} ')
           return redirect('login')
    
    form = RegisterForm()
    return render(request,'users/register.html' ,{'form':form})

def logout_view(request):
    auth_logout(request)
    return render(request,'users/logout.html')