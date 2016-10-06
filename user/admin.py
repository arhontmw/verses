from django.contrib import admin
from .models import Profile
# from django.contrib.auth.models import User

# Register your models here.


class ProfileAdmin(admin.ModelAdmin):
    list_display = ["get_username", "date_of_birth", "isadmin" ,"photo"]
    def get_username(self, obj):
         return obj.user.username
    get_username.short_description = "Пользователь"


admin.site.register(Profile, ProfileAdmin)
