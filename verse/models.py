from django.db import models
from django.core.validators import RegexValidator
# from django.template.defaultfilters import slugify
from author.models import Author
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.conf import settings

# Create your models here.
class Verse(models.Model):
    title = models.CharField(max_length = 150, verbose_name = "Заголовок")
    author = models.ForeignKey(Author, related_name = "verses", verbose_name = "Автор")
    year_of_writing = models.CharField(max_length = 200, blank = True, verbose_name = "Год написания",
                                        validators = [
                                            RegexValidator(
                                                regex = r'^\d{4}$',
                                                message = "You must enter a year",
                                                code = "Invalid year"
                                            )
                                        ])
    slug = models.SlugField(max_length = 50, db_index = True, unique = True, verbose_name='Идентификатор')
    text = models.TextField(blank = True, verbose_name = "Текст произведения")
    users_like = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="verses_liked", blank = True, verbose_name = "Понравилось пользователям" )
    created_date = models.DateTimeField(auto_now_add = True, verbose_name = "Дата создания")
    update_date = models.DateTimeField(auto_now = True, verbose_name = "Дата обновления")


    class Meta:
        verbose_name = "Произведение"
        verbose_name_plural = "Произведения"

    # def save(self, *args, **kwargs):
    #     # self.slug = slugify("{} {}".format(self.title, self.author))
    #     self.slug = slugify(self.title)
    #     super(Verse, self).save(*args, **kwargs)

    def __str__(self):
        return "{} ({}. {})".format(self.title, self.author.first_name[0], self.author.surname)

    def get_absolute_url_detail(self):
        return reverse("verse:verse_detail", args=[self.id, self.slug])
