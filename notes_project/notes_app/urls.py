from django.urls import path
from .views import create_note, show_notes

urlpatterns = [
    path('', create_note, name="create-data"),
    path('show/', show_notes, name="show"),
]
