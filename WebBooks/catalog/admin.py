from django.contrib import admin
from .models import Author, Book, Genre, Language, Status, BookInstance
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name')
    fields = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
admin.site.register(Author, AuthorAdmin)
#admin.site.register(Book)
admin.site.register(Genre)
admin.site.register(Language)
admin.site.register(Status)
#admin.site.register(BookInstance)

class BooksInstanceInline(admin.TabularInline):
    model = BookInstance


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title','genre','laguage','display_author')
    list_filter = ('genre','author')
    inlines = [BooksInstanceInline]

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('book', 'status')
    fieldsets = (
        ('Экземпляр книги', {'fields':('book','imprint', 'inv_nom')
                             }),
        ('Статус и окончание его действия', {
            'fields': ('status', 'due_back')
        }),
    )

