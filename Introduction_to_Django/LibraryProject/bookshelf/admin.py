from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Book

# Customize how the Book model appears in admin
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    search_fields = ('title', 'author')
    list_filter = ('publication_year',)

# Register the model with its custom admin configuration
admin.site.register(Book, BookAdmin)
