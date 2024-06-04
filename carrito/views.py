from django.shortcuts import render

# Create your views here..
def Carritos(request):
    return render(request, "carrito.html")