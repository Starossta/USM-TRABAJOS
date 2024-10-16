from django.shortcuts import render

# Create your views here.
def home(request):
    titulo='inicio'
    data ={
        'titulo':titulo
    }
    return render(request,'index.html',data)
