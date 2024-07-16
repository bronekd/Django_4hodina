from django.urls import reverse_lazy
from django.views.generic import DeleteView
from ..models import Book


class BookDeleteView(DeleteView):
    model = Book
    template_name = 'book_confirm_delete.html'
    success_url = reverse_lazy('book_list')