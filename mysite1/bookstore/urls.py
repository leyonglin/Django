
from django.urls import path, re_path, include

from bookstore import views

urlpatterns = [
    path('all_book',views.all_book),
    path('update_book/<int:book_id>',views.update_book),
    path('delete_book',views.delete_book),
]