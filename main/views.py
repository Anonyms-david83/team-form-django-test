from django.shortcuts import render, redirect
from django.http import Http404
from .models import Register
from django.contrib import messages

def home(request):
    template_name = 'main.html'
    return render(request, template_name)

def create(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        score = request.POST.get('score')

        try:
            Register.objects.create(fname=fname, lname=lname, score=score)
            messages.success(request, 'Registered successfully', 'success')
            return redirect('main_page')  # Redirect back to home page after successful registration
        except:
            messages.error(request, 'Registration unsuccessful, please try again', 'danger')
            return redirect('main_page')  # Redirect back to home page if registration fails
    else:
        raise Http404("Page not found")


