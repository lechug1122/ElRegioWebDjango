from django.shortcuts import render

# Create your views here.
def nuggets(request):
    return render(request, "Nuggets.html")