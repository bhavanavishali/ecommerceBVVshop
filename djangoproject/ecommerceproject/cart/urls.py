from . import views
from django.urls import path
app_name = 'cart'

urlpatterns = [
    path('add/<int:product_id>/',views.add_cart,name= 'add_cart'),
    path('',views.cart_details,name= 'cart_details'),
    path('remove/<int:product_id>/',views.cart_remove,name= 'cart_remove'),
    path('full_delete/<int:product_id>/',views.full_delete,name= 'full_delete'),
]