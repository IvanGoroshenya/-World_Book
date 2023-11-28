from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic, View

from .models import Book, Author, BookInstance
from django.views.generic import ListView, DetailView


def about(request):
    text_head = "Сведения о компании"
    name = 'OOO "Интелектуальные информационные системы"'
    rab1 = 'Разработка приложений на основе' \
           'систем искусственного интелекта'
    rab2 = 'Распознавания объектов дорожной инфраструктуры'
    rab3 = 'Создание графических АРТ-объектов на основе' \
           ' систем искусственного интелпекта'
    rab4 = 'Создание цифровых интерактивных книг, учебных пособий' \
           ' автоматизированных обучаIСЩИх систем'
    context = {'text_head': text_head, 'name': name,
               'raЬl': rab1, 'rаЬ2': rab2,
               'rаЬЗ': rab3, 'rаЬ4': rab4}
    return render(request, 'catalog/about.html', context)


def contact(request):
    text_head = 'Контакты'
    name = 'ООО "Интеллектуальные информационные системы"'
    address = 'Москва, ул. Планерная, д. 20, к. 1'
    tel = '495-345-45-45'
    email = 'iis info@mail.ru'
    context = {'text _ head': text_head,
              'name': name, 'address': address,
              'tel': tel,   'email': email}

    return render(request, 'catalog/contact.html', context)

def index(request):
    text_head = 'На нашем сайте вы можете nолучить книги в электронном виде'
# Данные о книгах и их количестве
    books = Book.objects.all()
    num_books = Book.objects.all() .count()
# Данные об экземплярах книг в БД
    num_instances = BookInstance.objects.all() .count()
# # Доступные книги (статус = 'На складе')
    num_instances_availabe = BookInstance.objects.filter(status__exact=2) .count()
# Данные об авторах книг
    authors = Author.objects
    num_authors = Author.objects.count()
# # Словарь для передачи данных в шаблон index.html
    context = {'text_head':text_head,
                 'books': books, 'num_books': num_books,
                'num_instances': num_instances,
                'num_instances_available': num_instances_availabe,
                'authors': authors, 'num_authors': num_authors}
# # передача словаря context с данными в шаблон
    return render(request, 'catalog/index.html', context)


class BookListView(ListView):
    model = Book
    contex_object_name = 'books'
    paginate_by = 3
    template_name = "my_books.html"

class BookDetailView(generic.DetailView):
    Model = Book
    def index(request):
        Book = BookDetailView.objects.all()
        return render(request, 'book_detail.html', {'book': Book})

    def detail(request, book):
        return HttpResponse(book)


class AuthorListView(ListView):
    model = Author

    paginate_by = 4


class AuthorDetailView(DetailView):
    model = Author
    contex_object_name = 'author-detail'
    template_name = "author_detail.html"

