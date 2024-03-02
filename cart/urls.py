from django.urls import path

from . import views

app_name = 'cart'


urlpatterns = [
    path('', views.cart_summary, name='cart_summary'),
    path('add/<int:item_id>/', views.cart_add, name='cart_add'),
    path('delete/<str:name>/', views.cart_delete, name='cart_delete'),
]
