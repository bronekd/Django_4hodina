from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path("list", BookListView.as_view(), name="book_list")
]