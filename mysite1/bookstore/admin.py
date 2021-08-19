from django.contrib import admin
from .models import Book,Author
# Register your models here.

class BookManager(admin.ModelAdmin):
    list_display = ['id','title','pub','price','market_price','is_active']
    list_display_links = ['title']
    list_filter = ['pub']
    search_fields = ['title']
    # list_display_links和list_editable是互斥的
    list_editable = ['price']
admin.site.register(Book,BookManager)

class AuthorManager(admin.ModelAdmin):
    list_display = ['id','name','age','email']
    # list_display_links = ['name']
    list_filter = ['name']
    search_fields = ['name']
    # list_display_links和list_editable是互斥的
    list_editable = ['name','age']
admin.site.register(Author,AuthorManager)