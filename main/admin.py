from django.contrib import admin
from . models import categories,News

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'image']

class NewsAd(admin.ModelAdmin):
    list_display = ['title', 'image', 'description']


admin.site.register(categories, CategoryAdmin)
admin.site.register(News, NewsAd)