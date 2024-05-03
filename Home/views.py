from django.shortcuts import render

# Create your views here.
def Homes(request):
    return render(request, "home.html")