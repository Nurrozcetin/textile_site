from django.urls import path

from event_reporting import views


urlpatterns = [
    path('create/', views.create_event, name="event_create"),
    path('delete/<int:id>', views.delete_event, name="event_delete"),
    path('list/', views.list_event, name="event_list"),
    path('edit/<int:id>', views.edit_event, name="event_edit")
]
