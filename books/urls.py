from django.urls import path

from books import views

urlpatterns = [
    path('book_list', views.book_list, name='book_list'),
    path('view/<int:pk>', views.book_view, name='book_view'),
    path('new', views.book_create, name='book_new'),
    path('edit/<int:pk>', views.book_update, name='book_edit'),
    path('delete/<int:pk>', views.book_delete, name='book_delete'),
    path('', views.home, name='home'),
    path('search_item',views.search_item, name="search_item"),
    path('index', views.index,name="aaa"),
]