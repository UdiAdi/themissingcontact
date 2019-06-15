from django.shortcuts import render
from django.shortcuts import redirect

def firstapp_view(request):
    return render(request, 'firstapp/first_page.html')

