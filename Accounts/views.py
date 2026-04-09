from django.shortcuts import render,redirect
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,AdminPasswordChangeForm
# Create your views here.

def register_view(request):
    if request.method == "POST":
        reg_form = UserCreationForm(request.POST)
        if reg_form.is_valid():
            user = reg_form.save()
            login(request,user)
            return redirect('Article:home')
    else:
        reg_form = UserCreationForm()
    return render(request,'register.html',{"Reg": reg_form})

def login_view(request):
    if request.method == "POST":
        log_form = AuthenticationForm(data=request.POST)
        if log_form.is_valid():
            user = log_form.get_user()
            login(request,user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('Article:home')
    else:
        log_form = AuthenticationForm()
    return render(request,'login.html',{"Log_form":log_form})

@login_required(login_url='Accounts:logger')
def logout_view(request):
    logout(request)
    return redirect('Article:home')
