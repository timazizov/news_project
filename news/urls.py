from django.urls import path, include
from rest_framework import routers

from news.views import NewsViewSet, CategoryViewSet

router = routers.DefaultRouter()
router.register(r'news', NewsViewSet)
router.register(r'categories', CategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
