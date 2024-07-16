from django.urls import path
from .views import *

urlpatterns = [
    path("list/", BookListView.as_view(), name="book_list"),
    path("create/", BookCreateView.as_view(), name="book_create"),
]