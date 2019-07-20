from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.home, name='home'),
    path('account/login/', LoginView.as_view(template_name='login.html'), name="login"),
    path('account/logout/', LoginView.as_view(template_name='logout.html'), name="logout"),
    
]
