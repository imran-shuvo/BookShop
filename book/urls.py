
from django.urls import path
from . import views


urlpatterns = [

    path('',views.show_book_list,name = 'book-list'),
    path('book-detail/<int:book_id>',views.book_details,name = 'book-detail'),
    path('add-category/',views.add_category,name = 'add-category'),
    path('delete-category/<int:cat_id>',views.add_category,name = 'delete-category'),
    path('category/',views.show_category,name = 'category'),
    path('category-book/<int:cat_id>',views.show_category_book,name = 'category-book'),
    path('add-book/',views.add_book,name = 'add-book'),
    path('edit-book/<int:book_id>',views.edit_book,name = 'edit-book'),
    path('delete-book/<int:book_id>',views.delete_book,name = 'delete-book'),

]
