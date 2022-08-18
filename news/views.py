from rest_framework import viewsets

from news.models import News, Category
from news.serializers import NewsSerializer, CategorySerializer
from news.utils import NewsPagination


class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    pagination_class = NewsPagination


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
