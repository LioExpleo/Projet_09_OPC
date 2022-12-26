from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


# Create your views here.
def hello_critique(request):
    return HttpResponse('<h1>Hello LitReview critique!</h1>')
