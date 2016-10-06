from django.db import models
from verse.models import Verse
from django.contrib.auth.models import User

# Create your models here.
class Comment(models.Model):
    verse = models.ForeignKey(Verse, related_name="comments", verbose_name="Произведение")
    user = models.ForeignKey(User, related_name="comments", verbose_name ="Пользователь")
    text = models.TextField(max_length = 140, blank = True, verbose_name = "Текст комментария")
    created_date = models.DateTimeField(auto_now_add = True, verbose_name = "Дата создания")
    update_date = models.DateTimeField(auto_now = True, verbose_name = "Дата обновления")
    active = models.BooleanField(default=True, verbose_name = "Активен")

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
        ordering = ("-update_date",)

    def __str__(self):
        return "Комментарий пользователя {} к '{}' (от {})".format(self.user.username, self.verse.title, self.created_date)
