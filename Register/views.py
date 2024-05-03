from django.shortcuts import render

# Create your views here.
def Registers(request):
    return render(request, "register.html")