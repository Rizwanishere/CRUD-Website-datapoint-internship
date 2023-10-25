from django.shortcuts import render

# Create your views here.
def gro(request):
    return render(request,'grocery.html',)