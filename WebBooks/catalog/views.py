from django.shortcuts import render
from django.http import HttpResponse
from .models import BookInstance, Book, Author, Genre
from django.views import generic

class BookDetailView(generic.DetailView):
    model = Book


class BookListViews(generic.ListView):
    model = Book
    paginate_by = 3

class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 4
def index(request):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_instances_available = BookInstance.objects.filter(status__exact=2).count()
    num_authors = Author.objects.count()

    return render(request, 'index.html',
                  context={'num_books':num_books,
                           'num_instances':num_instances,
                           'num_instances_available': num_instances_available,
                           'num_authors': num_authors},
                  )


# Create your views here.
