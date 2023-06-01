
from django.urls import path
from main import views

urlpatterns = [
    path('', views.MainPageView.as_view(), name='MainPage'),
    path('createHousehold/', views.createHousehold, name='CreateHousehold'),
    path('joinHousehold/', views.joinHousehold, name='JoinHousehold'),
    path('joinHousehold/<str:name>/', views.enterHousehold, name='EnterHousehold'),
    path('joinHousehold/<str:name>/password/',
         views.enterHouseholdPassword, name='EnterHouseholdPassword'),
    path('household/<str:name>/', views.HouseholdView.as_view(), name='Household'),
    path('household/<str:name>/addExpense/',
         views.addExpense, name='AddExpense'),
    path('household/<str:name>/deleteExpense/<int:id>/',
         views.deleteExpense, name='DeleteExpense'),
    path('household/<str:name>/addProduct/',
         views.addProduct, name='AddProduct'),
    path('household/<str:name>/deleteProduct/<int:id>/',
         views.deleteProduct, name='DeleteProduct'),
    path('household/<str:name>/addTask/', views.addTask, name='AddTask'),
    path('household/<str:name>/deleteTask/<int:id>/',
         views.deleteTask, name='DeleteTask'),
    path('household/<str:name>/leaveHousehold',
         views.leaveHousehold, name='leaveHousehold'),
]
