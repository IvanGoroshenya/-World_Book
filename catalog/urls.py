
from django.urls import path
from django.contrib import admin
from .import views
from django.urls import path

from .views import index

urlpatterns = [
    path('', views.index, name = 'index'),

    path('books', views.BookListView.as_view(), name='books'),
    path('books/<int:pk>/', views.BookDetailView.as_view(), name='books'),

    path('author/', views.AuthorListView.as_view(), name='author-list'),
    path('author/<int:pk>/',views.AuthorDetailView.as_view(), name ='author-list'),

    path('about/', views.about, name = 'about'),
    path('contact/',views.contact, name='contact'),

]

