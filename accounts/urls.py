
from django.urls import path
from accounts import views

urlpatterns = [
    path('createAccount/', views.CreateAccountView.as_view(), name='CreateAccount'),
    path('', views.LoginView.as_view(), name='Login'),
    path('logout/', views.LogoutView.as_view(), name='Logout'),

]
