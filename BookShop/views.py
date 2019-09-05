from django.shortcuts import render,redirect



def HomePage(request):
    return render(request,'try.html')
