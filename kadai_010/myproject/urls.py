from django.contrib import admin
from django.urls import path
from crud.views import ProductListView, ProductDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('crud/', ProductListView.as_view(), name='product_list'),
    path('crud/detail/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
]
