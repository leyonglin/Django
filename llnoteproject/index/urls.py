

from django.urls import path

from index import views

urlpatterns = [
    path('index_view/', views.index_view),
]