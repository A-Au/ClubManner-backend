from django.shortcuts import render
from django.http import HttpResponse
from model.models import Product, Profile, PantsFitting, ProductCategory, Province, ShirtFitting, Size, Style, Brand, Store
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login, authenticate
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.template import RequestContext


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1'],
                email=form.cleaned_data['email']
                )
            return HttpResponseRedirect('/form/details/')
    else:
        form=RegistrationForm

    return render(request, 'register.html', { 'form': form })

def register_details(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/form/success/')
    else:
        form = SignupForm

    return render(request, 'register.html', { 'form': form })


def register_success(request):
    return render(request, 'success.html')


def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/form/home/')


@login_required(login_url = '/form/login/')
def get_home(request):
    return render(request, 'home.html', { 'user': request.user })


'''def get_signup(request):
    if request.method == 'POST':
        signupForm = SignupForm(request.POST)

        if signupForm.is_valid():
            signupForm.save()

            return HttpResponseRedirect('/REPLACE WITH A LEGIT PATH')
    else:
        signupForm = SignupForm()

    return render(request, 'signup.html', {'form': signupForm})

def get_userUpdate(request):
    if request.method == 'POST':
        userUpdateForm = ProfileUpdateForm(request.POST)

        if userUpdateForm:
            userUpdateForm.save()

            return HttpResponseRedirect('')

    else:
        userUpdateForm = ProfileUpdateForm()

    return render(request, 'profile.html', {'form': userUpdateForm})
    

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'success.html')
    else:
    '''