from django.shortcuts import render

# Create your views here.
def sender(request):
    return render(request,'sender.html')