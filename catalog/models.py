from django.db import models
from django.urls import reverse

# Жанр книги
class Genre(models.Model):
    name = models.CharField(max_length=200,
                            help_text='Введите жанр книги',
                            verbose_name='Жанр книги')
    def __str__(self):
        return self.name


# язык книги
class Language(models.Model):
    name = models.CharField(max_length=20,
                            help_text='Введите язык книги',
                            verbose_name='Язык книги')
    def __str__(self):
        return self.name


# издательство
class Publisher(models.Model):
    name = models.CharField(max_length=20,
                            help_text=" Введите наименование издательства",
                            verbose_name="Издательство")
    def __str__(self):
        return self.name

#Год
class Year(models.Model):
    name = models.CharField(max_length=20,
                            help_text='Введите год названия',
                            verbose_name='Год издания')
    def __str__(self):
        return self.name



class Summary(models.Model):
    name = models.TextField(max_length=500,
                            help_text="Введите краткое описание книги",
                            verbose_name="Описание")
    def __str__(self):
        return  self.name


class Isbn(models.Model):
    name = models.CharField(max_length=13,
                            help_text="Должно содержать 13 символов",
                            verbose_name="ISBN книги")
    def __str__(self):
        return self.name

class Price(models.Model):
    name = models.DecimalField(decimal_places=2, max_digits=7,
                                help_text="Введите цену книги",
                                verbose_name="Цeнa (руб.")
class Photo(models.Model):
    name = models.ImageField(upload_to='images',
                              help_text="Введите изображение обложки",
                              verbose_name="Изображение обложки")
    def __str__(self):
        return self.name




# авторы
class Author(models.Model):
    first_name = models.CharField(max_length=100,
                                 help_text="Введите имя автора",
                                 verbose_name="Имя автора")
    last_name = models.CharField(max_length=100,
                                  help_text="Введите фамилию автора",
                                  verbose_name="Фамилия автора")
    date_of_birth = models.DateField(help_text="Введите дату рождения",
                                    verbose_name="Дaтa рождения",
                                    null=True, blank=True)
    about = models.TextField(help_text="Bвeдитe сведения об авторе",
                            verbose_name="Сведения об авторе")
    photo = models.ImageField(upload_to='images',
                              help_text="Введите фото автора",
                              verbose_name="Фoтo автора",
                              null=True, blank=True)
    def __str__(self):
        return self.last_name


#
# книги
class Book(models.Model):

    title = models.CharField(max_length=200,
                            help_text="Введите название книги",
                            verbose_name="Haзвaниe книги")
    genre = models.ForeignKey('Genre',
                             on_delete=models.CASCADE,
                             help_text=" Выберите жанр для книги",
                             verbose_name="Жанр книги", null=True)
    language = models.ForeignKey('Language',
                                on_delete=models.CASCADE,
                                help_text="Выберите язык книги",
                                verbose_name="Язык книги", null=True)
    publisher =models.ForeignKey('Publisher',
                                on_delete=models.CASCADE,
                                help_text="Выберите издательство",
                                verbose_name ="Издательство", null=True)
#
    year = models.CharField(max_length=4,
                            help_text='Введите год названия',
                            verbose_name='Год издания', null=True)
    author = models.ManyToManyField('Author',
                                    help_text='Выберите автора книги',
                                    verbose_name='Автор книги')
    summary = models.TextField(
                              help_text="Введите краткое описание книги",
                              verbose_name="Описание",null=True)
    isbn = models.CharField(max_length=13,
                            help_text="Должно содержать 13 символов",
                            verbose_name="ISBN книги", null=True)

    price = models.DecimalField(decimal_places=2, max_digits=7,
                                help_text="Введите цену книги",
                                null=True)
    photo = models.ImageField(upload_to='images',
                              help_text="Введите изображение обложки",
                              verbose_name="Изображение обложки", null=True)

    def display_author(self):
        return ', '.join([author.last_name for author in self.author.all()])

    display_author.short_description = 'Авторы'


    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])
#
# состояние экземпляра книги
class Status(models.Model):
    name = models.CharField(max_length=20,
                            help_text="Введите статус экземпляра книги",
                            verbose_name="Cтaтyc экземпляра книги")
    def __str__(self):
        return self.name


# экземпляр книги
class BookInstance(models.Model):

    book = models.ForeignKey('Book',
                            on_delete=models.CASCADE, null=True)
    inv_nom = models.CharField(max_length=20,
                               help_text="Введите инвентарный номер экземпляра",
                               verbose_name= "Инвентарный номер",null=True)
    status = models.ForeignKey('Status',
                               on_delete=models.CASCADE,
                               null=True,
                               help_text='Изменить состояние экземпляра',
                               verbose_name="Cтaтyc экземпляра книги")
    due_back = models.DateField(null=True,
                                blank=True,
                                help_text="Введите конец срока статуса",
                                verbose_name="Дaтa окончания статуса")
    # Метаданные

    class Meta:
        ordering = ["due_back"]

    def __str__(self):
        return '%s %s %s' % (self.inv_nom, self.book, self.status)

