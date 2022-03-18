from django.contrib import admin
from .models import Author, Book, BookInstance, Genre, Language

# Register your models here.
class BookInstanceInline(admin.TabularInline):
    model = BookInstance
    extra = 0

class BookInline(admin.TabularInline):
    model = Book
    extra = 0
    exclude = ['summary']



class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', 'date_of_birth', 'date_of_death']

    inlines = [BookInline]



@admin.register(Book) #does exactly the same thing as admin.site.register()
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')

    inlines = [BookInstanceInline]

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'due_back', 'id')
    list_filter = ('status', 'due_back')

    fieldsets = (
        ('None', {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )

#admin.site.register(Book)
#admin.site.register(Author)
admin.site.register(Author, AuthorAdmin)

#admin.site.register(BookInstance)
admin.site.register(Genre)
admin.site.register(Language)
