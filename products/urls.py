from django.urls import path

from products import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('products/<int:code>/', views.ProductDetailView.as_view(), name='product-detail'),
    path('products/', views.ProductListView.as_view(), name='product-list'),
]
