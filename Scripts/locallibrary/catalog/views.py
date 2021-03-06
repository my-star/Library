from django.shortcuts import render
from .models import BookInstance, Book, Author, Genre
from django.views import generic

# Create your views here.
def index(request):
    """
    View function for home page of site
    """
    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    # Available Books (status = 'a')
    num_instance_available = BookInstance.objects.filter(status__exact='a').count()
    num_authors = Author.objects.count()  # The 'all()' is implied by default.
    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'index.html',
        context={'num_books': num_books, 'num_instances': num_instances,
                 'num_instance_available': num_instance_available, 'num_authors': num_authors}
    )
class BookListView(generic.ListView):
    model = Book
    context_object_name = "book_list"
    queryset = Book.objects.all()
    template_name = 'book_list.html'

class BookDetailView(generic.DetailView):
    model = Book
    template_name = 'book_detail.html'

