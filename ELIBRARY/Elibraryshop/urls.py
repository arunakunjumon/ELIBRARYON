
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('index/',views.index,name='index'),

    path('library/',views.library,name='library'),
    path('my_library/',views. my_library, name='my_library'),
    path('library/<int:lb>/', views.library_details, name='library_details'),

    path('books/',views.books,name='books'),
    path('my_books/', views.my_books, name='my_books'),
    path('book/<int:bk>/', views.book_details, name='book_details'),
    path('add_book/',views.add_book,name='add_book'),
    path('book_list/',views.book_list, name='book_list'),

    path('adminlogin/',views.adminlogin,name='adminlogin'),
    path('adminhome/',views.adminhome, name='adminhome'),

    path('user_register/',views.user_register,name='user_register'),
    path('user_login/',views.user_login,name='user_login'),
    path('user_home/',views.user_home, name='user_home'),
    path('user_profile/', views.profile, name='user_profile'),
    path('update_profile/',views.update_profile, name='update_profile'),
    path('proupdate/',views.user_proupdate,name='proupdate'),
    path('user_list/',views.user_list, name='user_list'),

    path('search/',views.search_books, name='search_books'),

]
