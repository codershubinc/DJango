from django.shortcuts import render  # type: ignore

# Create your views here.

def login(request):
    return render(request, 'appwrite_auth/login.html')

def signup(request):
    return render(request, 'appwrite_auth/signup.html')