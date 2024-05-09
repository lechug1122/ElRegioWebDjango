from django.shortcuts import render

# Create your views here.
def Samplers(request):
    return render(request, "samples.html")