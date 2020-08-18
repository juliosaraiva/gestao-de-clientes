from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import logout
from django.views import View

def home(request):
    return render(request, 'home.html')

def getLogout(request):
    logout(request)
    return redirect('home')

class MyView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("Hello, World!")
