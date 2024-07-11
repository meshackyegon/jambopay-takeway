from django.urls import path
from .views import CategoryListCreate, ItemListCreate, ItemDetail

urlpatterns = [
    path('categories/', CategoryListCreate.as_view(), name='category-list-create'),
    path('items/', ItemListCreate.as_view(), name='item-list-create'),
    path('items/<int:pk>/', ItemDetail.as_view(), name='item-detail'),
]
