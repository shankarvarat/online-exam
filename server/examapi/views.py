from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
def hello(request):
  return JsonResponse({'response_text':'hello world!'})