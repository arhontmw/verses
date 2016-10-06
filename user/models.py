from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name="profile", verbose_name = "Пользователь")
    date_of_birth = models.DateField(blank=True, null=True, verbose_name = "Дата рождения")
    GENDER_CHOICES = (("М", "Мужской"), ("Ж", "Женский"))
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, verbose_name = 'Пол',
                              null=True, blank=True)
    isadmin = models.BooleanField(default=False, verbose_name = "Права администратора")
    photo = models.ImageField(upload_to="users/%Y/%m/%d", blank=True, verbose_name = "Фотография")
    created_date = models.DateTimeField(auto_now_add=True, verbose_name = "Дата создания профиля")
    updated_date = models.DateTimeField(auto_now=True, verbose_name = "Дата последнего изменения профиля")

    def __str__(self):
        return "Profile for user {}".format(self.user.username)

    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"
