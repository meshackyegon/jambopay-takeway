# from django.shortcuts import render

# # Create your views here.
# from rest_framework import generics
# from .models import Category, Item
# from .serializers import CategorySerializer, ItemSerializer

# class CategoryListCreate(generics.ListCreateAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer

# class ItemListCreate(generics.ListCreateAPIView):
#     queryset = Item.objects.all()
#     serializer_class = ItemSerializer

# class ItemDetail(generics.RetrieveAPIView):
#     queryset = Item.objects.all()
#     serializer_class = ItemSerializer

from rest_framework import generics, filters
from .models import Category, Item
from .serializers import CategorySerializer, ItemSerializer

class CategoryListCreate(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ItemListCreate(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'unique_attributes']

class ItemDetail(generics.RetrieveAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
