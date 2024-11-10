from django.shortcuts import render

# Create your views here.
def about(request):
    return render(request, template_name= 'about.html')
def base(request):
    return render(request,template_name='base.html')
def contact(request):
    return render(request, template_name='contact.html')
def home(request):
    return render(request,template_name='home.html')