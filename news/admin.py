from django.contrib import admin

from news.models import Category, News


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', ]
    list_filter = ['name', ]
    search_fields = ['name', ]


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'created_at', 'updated_at', ]
    list_filter = ['category', ]
    search_fields = ['title', 'body', ]
