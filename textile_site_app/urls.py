from django.urls import path

from textile_site_app import views


urlpatterns = [
    path('', views.textile, name="items" ),
    path('create/', views.create_item, name="item_create"),
    path('delete/<int:id>', views.delete_item, name="item_delete"),
    path('search/', views.search, name="search"),
    #path('items/<name:name>', views.getItemByCategory, name='items_by_category')
]
