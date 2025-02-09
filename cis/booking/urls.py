from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.reservation_view, name='reservation'),
    path('book_multiple/', views.book_multiple, name='book_multiple'),
    path('cancel/<int:reservation_id>/', views.cancel_reservation, name='cancel_reservation'),
    path('book/<int:shelf_id>/', views.book_shelf, name='book_shelf'),
    path('cancel_reservation_group/', views.cancel_reservation_group, name='cancel_reservation_group'),

]
