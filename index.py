from django.shortcuts import render
from django.shortcuts import redirect

def home(request):
    return render(request, 'home.html')

def facebook(request):
    return render(request,'facebook.html')

def twitter(request):
    return render(request,'twitter.html')

def instagram(request):
    return render(request,'instagram.html')

def linkedin(request):
    return render(request,'linkedin.html')

def signup(request):
    return render(request,'signup.html')