# from django.shortcuts import render

# Create your views here.
# # myapp/views.py
# from django.http import HttpResponse

# def home(request):
#     return HttpResponse("Hello, Django!")

# myapp/views.py
# from django.shortcuts import render

# def home(request):
#     return render(request, '.index.html')

from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, Django!")
