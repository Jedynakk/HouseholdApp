from django.shortcuts import render, redirect, HttpResponse
from accounts.forms import AddUserForm, LoginForm
from django.views import View
from django.contrib.auth import authenticate, login, logout
from main.models import Household, Housemate
from django.core.exceptions import ObjectDoesNotExist, ValidationError


class CreateAccountView(View):
    def get(self, request):
        form = AddUserForm()
        return render(request, 'CreateAccount.html', {'form': form})

    def post(self, request):
        form = AddUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            return redirect('Login')
        return render(request, 'CreateAccount.html', {'form': form})


class LoginView(View):
    def get(self, request):
        return render(request, 'login.html', {'form': LoginForm()})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request,
                                username=username,
                                password=password)
            login(request, user)
            currentUser = request.user
            try:
                household = Household.objects.get(creator_id=currentUser.pk)
            except ObjectDoesNotExist:
                housemate = Housemate.objects.filter(user_id=currentUser.pk)
                if housemate.exists():
                    housemate = Housemate.objects.get(user_id=currentUser.pk)
                    household = housemate.houseHold.name
                    return redirect('Household', household)
                else:
                    return redirect("MainPage")
            else:
                return redirect('Household', household.name)
        return render(request, 'account/login.html', {'form': LoginForm()})


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('Login')
