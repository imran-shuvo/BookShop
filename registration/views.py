from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import UserCreateForm
from buy.views import del_cart

# Create your views here.
def user_signup(request):
    if request.method =='POST':

        form = UserCreateForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            # username = form.cleaned_data.get('username')
            # raw_password = form.cleaned_data.get('password1')
            # user = authenticate(username=username, password=raw_password)
            # login(request, user)
            return redirect('login')
        else:
            return HttpResponse("Username or password incorrect")

        # user = authenticate(username=username,password = password)
    else :
        form = UserCreateForm()
        context = {'signup_form':form}
        return render(request,'registration/signup.html',context)

def user_login(request):
    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password = password)
        if user:
            login(request, user)
            del_cart(True)
            # mylist = []
            # xfunc(mylist)
            return redirect('book-list')
        else:
            return HttpResponse("Username or password incorrect")

    return render(request, 'registration/login.html')

def user_logout(request):
    del_cart(True)
    logout(request)
    return redirect('login')

def user_profile(request):
    return render(request,'registration/profile.html')
