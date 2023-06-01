from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from main.forms import CreateHouseholdForm, JoinHouseholdForm, AddExpenseForm, AddProductForm, AddTaskForm
from django.views import View
from main.models import Household, Housemate, Task, Expense, Product
from django.core.exceptions import ObjectDoesNotExist
import random
import string


class MainPageView(View):
    def get(self, request):
        currentUser = request.user
        if currentUser.is_authenticated:
            createForm = CreateHouseholdForm()
            joinForm = JoinHouseholdForm()
        else:
            return render(request, 'LoginValidation.html')
        return render(request, 'MainPage.html', {'createForm': createForm, 'joinForm': joinForm})


def createHousehold(request):
    currentUser = request.user
    createForm = CreateHouseholdForm(request.POST)
    if currentUser.is_authenticated:
        if createForm.is_valid():
            form = createForm.save(commit=False)
            form.creator_id = currentUser.pk
            characters = string.ascii_letters + string.digits
            randomPassword = ''.join(random.choice(characters)
                                     for i in range(8))
            form.password = randomPassword
            householdName = form.name
            form.save()
    else:
        return render(request, 'LoginValidation.html')
    return redirect('Household', householdName)


def joinHousehold(request):
    currentUser = request.user
    if currentUser.is_authenticated:
        if request.method == "POST":
            HouseholdName = request.POST["HouseholdName"]
            household = Household.objects.get(name=HouseholdName)
    else:
        return render(request, 'LoginValidation.html')
    return redirect('LoginValidation', household.name)


def enterHousehold(request, name):
    currentUser = request.user
    if currentUser.is_authenticated:
        houseHold = Household.objects.get(name=name)
    else:
        return render(request, 'LoginValidation.html')
    return render(request, 'LoginValidation.html', {'houseHold': houseHold, 'currentUser': currentUser})


def enterHouseholdPassword(request, name):
    houseHold = Household.objects.get(name=name)
    currentUser = request.user
    if currentUser.is_authenticated:
        if request.method == "POST":
            password = request.POST["password"]
            if password == houseHold.password:
                if currentUser.id != houseHold.creator_id:
                    Housemate.objects.create(
                        houseHold_id=houseHold.pk, user_id=currentUser.pk)
    else:
        return render(request, 'LoginValidation.html')
    return redirect('Household', houseHold.name)


class HouseholdView(View):
    def get(self, request, name):
        currentUser = request.user
        household = Household.objects.get(name=name)
        householdUsers = []
        householdUsers.append(household.creator_id)
        housemates = Housemate.objects.filter(houseHold_id=household.id)
        for housemate in housemates:
            householdUsers.append(housemate.user_id)
        if currentUser.is_authenticated:
            if currentUser.id in householdUsers:
                addExpenseForm = AddExpenseForm()
                addProductForm = AddProductForm()
                addTaskForm = AddTaskForm()
                expenses = Expense.objects.filter(household_id=household.pk)
                products = Product.objects.filter(household_id=household.pk)
                tasks = Task.objects.filter(household_id=household.pk)
                return render(request, 'Household.html', {'household': household, 'currentUser': currentUser, 'addExpenseForm': addExpenseForm, 'addProductForm': addProductForm, 'addTaskForm': addTaskForm, 'expenses': expenses, 'products': products, 'tasks': tasks, 'householdUsers': householdUsers})
            else:
                return render(request, 'HouseholdValidation.html')
        else:
            return render(request, 'LoginValidation.html')


def addExpense(request, name):
    addExpenseForm = AddExpenseForm(request.POST)
    household = Household.objects.get(name=name)
    if addExpenseForm.is_valid():
        form = addExpenseForm.save(commit=False)
        form.household_id = household.id
        form.save()
    return redirect('Household', household.name)


def deleteExpense(request, name, id):
    household = Household.objects.get(name=name)
    expense = Expense.objects.get(id=id)
    expense.delete()
    return redirect('Household', household.name)


def addProduct(request, name):
    addProductForm = AddProductForm(request.POST)
    household = Household.objects.get(name=name)
    if addProductForm.is_valid():
        form = addProductForm.save(commit=False)
        form.household_id = household.id
        form.save()
    return redirect('Household', household.name)


def deleteProduct(request, name, id):
    household = Household.objects.get(name=name)
    product = Product.objects.get(id=id)
    product.delete()
    return redirect('Household', household.name)


def addTask(request, name):
    addTaskForm = AddTaskForm(request.POST)
    household = Household.objects.get(name=name)
    if addTaskForm.is_valid():
        form = addTaskForm.save(commit=False)
        form.household_id = household.id
        form.save()
    return redirect('Household', household.name)


def deleteTask(request, name, id):
    household = Household.objects.get(name=name)
    task = Task.objects.get(id=id)
    task.delete()
    return redirect('Household', household.name)


def leaveHousehold(request, name):
    currentUser = request.user
    household = Household.objects.get(name=name)
    if currentUser.pk == household.creator_id:
        household.delete()
        return redirect('MainPage')
    else:
        housemate = Housemate.objects.get(user_id=currentUser.pk)
        housemate.delete()
        return redirect('MainPage')
