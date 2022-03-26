from django.shortcuts import render
from .models import Book, Genre, Author, BookInstance
from django.views import generic

# Create your views here.
def index(request):
    """"View function for home page site."""

    #Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    #Available books (status = 'a', as defined in models.py)
    num_instances_available  = BookInstance.objects.filter(status__exact='a').count()

    #The 'all()' is implied by default.
    num_authors = Author.objects.count()

    #number of visits to this view, as counted in the session variable
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    #Generate counts of genre and books that contains a particular word.
    #genre_word = 'Fiction'
    #book_word = 'Senhor'
    #num_particular_genre = Genre.objects.filter(name__icontains=genre_word).count()
    #num_particular_book = Book.objects.filter(title__icontains=book_word).count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_visits': num_visits,
    }

    #Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)


class BookListView(generic.ListView):
    """Generic class-based view for a list of books."""
    model = Book
    paginate_by = 5

class BookDetailView(generic.DetailView):
    """Generic class-based detail view for a book."""
    model = Book

class AuthorListView(generic.ListView):
    """Generic class-based view for a list of authorsm."""
    model = Author
    paginate_by = 5

class AuthorDetailView(generic.DetailView):
    """Generic class bases detail view for a author."""
    model = Author