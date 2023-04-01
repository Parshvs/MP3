from django.shortcuts import render,HttpResponse,redirect

# Create your views here.
def homepage(request):
    return render(request,'index.html')

def signin(request):
    return render(request,'signin.html')