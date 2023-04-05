from django.shortcuts import render

# Create your views here.
def index(request, item=None):

    return render(request, 'index.html', {'item':item})