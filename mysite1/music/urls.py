
from django.urls import path, re_path, include

from music import views

urlpatterns = [
    # http://127.0.0.1/music/index
    path('index',views.index_view),

    ]