from django.urls import path
from . import views 
import accounts.views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    
    path('', views.indexView, name="accounts"),
    path('dashboard/', views.dashboardView, name="dashboard"),
    path('login/', LoginView.as_view(), name="login_url"),
    path('register/', views.registerView, name="register_url"),
    path('logout/', LogoutView.as_view(next_page='dashboard'), name="logout"),
    path('logout/', LogoutView.as_view(next_page='dashboard'), name="logout"),
]