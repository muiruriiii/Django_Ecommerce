from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.store, name="store"),
    path('cart/', views.cart, name="cart"),
    path('update_item/', views.updateItem, name="checkout"),
    path('checkout/', views.checkout, name="checkout"),
]