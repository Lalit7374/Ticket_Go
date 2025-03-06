# booking/urls.py
# booking/urls.py

from django.urls import path
from . import views  

urlpatterns = [
    path('', views.home, name='home'),  # Home view should map to '' (root URL)
    path('book/', views.book_ticket, name='book_ticket'),
    path('cancel/', views.cancel_ticket, name='cancel_ticket'),
    path('show_booked_ticket/', views.show_booked_ticket, name='show_booked_ticket'),
    path('undo_cancel/', views.undo_cancel, name='undo_cancel'),
]
