from django.contrib import admin
from .models import Verse
from author.models import Author
# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
    search_fields = ["surname"]
    list_display = ["surname", "first_name", "last_name", "date_of_birth", "date_of_death", 'created_date', 'update_date']
    list_filter = ["created_date", 'update_date']
    ordering = ("date_of_birth", "date_of_birth")
    prepopulated_fields = {"slug": ("surname", "first_name")}


class VerseAdmin(admin.ModelAdmin):
    model = Verse
    search_fields = ["title", 'author']
    list_display = ["title", "author", "year_of_writing", 'created_date', 'update_date']
    list_filter = ["created_date", 'update_date']
    ordering = ("title",)
    prepopulated_fields = {"slug": ("title", "author", "year_of_writing")}

    # def author_surname(self, obj):
    #     return obj.author.surname
    # author_surname.short_description = "Автор"
    # author_surname.admin_order_field = "author"


admin.site.register(Author, AuthorAdmin)
admin.site.register(Verse, VerseAdmin)
