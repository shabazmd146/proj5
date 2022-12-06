from django.shortcuts import render

# Create your views here.

def index(request):
    context = {'msg':'this is index page'}
    return render(request,'app1/index.html',context)
