
from django.urls import path

from user import views

urlpatterns = [
    path('reg_view', views.reg_view),
    path('login_view', views.login_view),
]
