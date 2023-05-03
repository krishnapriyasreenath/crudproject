from django.urls import path,include
from .import views

urlpatterns = [
    path('',views.load_page,name="load_page"),
    path('adddb',views.adddb,name="adddb"),
    path('show_product_details',views.show_product_details,name="show_product_details"),
    path('editpage/<int:pk>',views.editpage,name="editpage"),
    path('edit_product_details/<int:pk>',views.edit_product_details,name="edit_product_details"),
    path('deletepage/<int:pk>',views.deletepage,name="deletepage")

    
]