from django.urls import path
from .views import product_list, product_detail, category_detail, category_list, category_products
urlpatterns = [
    path('products/', product_list),
    path('products/<int:product_id>/', product_detail),
    path('categories/', category_list),
    path('categories/<int:category_id>/', category_detail),
    path('categories/<int:category_id>/products/', category_products),
 ]