
from django import forms
from main.models import Household, Expense, Product, Task


class CreateHouseholdForm(forms.ModelForm):
    class Meta:
        model = Household
        fields = ['name']
        labels = {
            'name': "",
        }
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Name your new household', 'class': 'field'}), }


class JoinHouseholdForm(forms.ModelForm):
    class Meta:
        model = Household
        fields = ['name']
        labels = {
            'name': "",
        }
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'What for?', 'class': 'field'}), }


class DateInput(forms.DateInput):
    input_type = 'date'


class AddExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['name', 'charge', 'until']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'What for?', 'class': 'field'}),
            'charge': forms.NumberInput(attrs={'placeholder': 'How much?', 'class': 'field'}),
            'until': DateInput(attrs={'placeholder': 'Set date', 'class': 'field'}),
        }
        labels = {
            'name': "",
            'charge': "",
            'until': ""
        }


class AddProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'quantity', 'unit']
        labels = {
            'name': "",
            'quantity': "",
            'unit': ""
        }
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Name', 'class': 'field'}),
            'quantity': forms.NumberInput(attrs={'class': 'field'}),
            'unit': forms.Select(attrs={'class': 'field'}),
        }


class AddTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['text', 'until']
        widgets = {
            'until': DateInput(attrs={'class': 'field'}),
            'text': forms.TextInput(attrs={'placeholder': 'What to do?', 'class': 'field'})
        }
        labels = {
            'text': "",
            'until': "",
        }
