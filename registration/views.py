from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def user_signup(request):
    if request.method =='POST':
        form = UserCreationForm(request.POST)
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
        form = UserCreationForm()
        context = {'signup_form':form}
        return render(request,'registration/signup.html',context)

def user_login(request):
    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password = password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse("Username or password incorrect")

    return render(request, 'registration/login.html')

def user_logout(request):
    logout(request)
    return redirect('home')
