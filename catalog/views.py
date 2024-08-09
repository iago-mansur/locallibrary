from django.shortcuts import render
from .models import Book, Author, BookInstance, Genre, Language

from django.views import generic


def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    # The 'all()' is implied by default.
    num_authors = Author.objects.count()

    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_visits': num_visits,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)


class BookListView(generic.ListView):
    """Generic class-based view for a list of books."""
    model = Book
    paginate_by = 10



class BookDetailView(generic.DetailView):
    """Generic class-based detail view for a book."""
    model = Book


class AuthorListView(generic.ListView):
    """Generic class-based list view for a list of authors."""
    model = Author
    paginate_by = 10


class AuthorDetailView(generic.DetailView):
    """Generic class-based detail view for an author."""
    model = Author


class GenreDetailView(generic.DetailView):
    """Generic class-based detail view for a genre."""
    model = Genre


class GenreListView(generic.ListView):
    """Generic class-based list view for a list of genres."""
    model = Genre
    paginate_by = 10


class LanguageDetailView(generic.DetailView):
    """Generic class-based detail view for a genre."""
    model = Language


class LanguageListView(generic.ListView):
    """Generic class-based list view for a list of genres."""
    model = Language
    paginate_by = 10


class BookInstanceListView(generic.ListView):
    """Generic class-based view for a list of books."""
    model = BookInstance
    paginate_by = 10


class BookInstanceDetailView(generic.DetailView):
    """Generic class-based detail view for a book."""
    model = BookInstance