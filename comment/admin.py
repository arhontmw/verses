from django.contrib import admin
from .models import Comment
# Register your models here

class CommentAdmin(admin.ModelAdmin):
    list_display = ("update_date", "user", "verse", "active")
    list_filter = ("created_date", "update_date")
    search_fields = ("user", "verse")

admin.site.register(Comment, CommentAdmin)
