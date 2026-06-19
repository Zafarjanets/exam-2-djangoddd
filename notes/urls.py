from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact, name='notes'),
    path('create-notes', views.create_note, name='create_notes'),
    path('update-notes/<int:pk>', views.update_note, name='update_notes'),
    path('delete-notes/<int:pk>', views.delete_note, name='delete_notes')
]
