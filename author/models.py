from django.db import models
# from django.template.defaultfilters import slugify
from django.core.urlresolvers import reverse

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length = 30, verbose_name = "Имя")
    last_name = models.CharField(max_length = 30, verbose_name = "Отчество")
    surname = models.CharField(max_length = 30, verbose_name = "Фамилия")
    slug = models.SlugField(max_length = 50, db_index = True, unique = True, verbose_name='Идентификатор')
    date_of_birth = models.DateField(verbose_name = "Дата рождения")
    date_of_death = models.DateField(verbose_name = "Дата смерти")
    biography = models.TextField(blank=True, verbose_name = "Биография")
    photo = models.ImageField(upload_to = "authors/%Y/%m/%d", blank=True)
    created_date = models.DateTimeField(auto_now_add = True, verbose_name = "Дата создания")
    update_date = models.DateTimeField(auto_now = True, verbose_name = "Дата обновления")

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"

    def __str__(self):
        return "{} {} ({}-{})".format(self.first_name, self.surname, self.date_of_birth.year, self.date_of_death.year)

    # def save(self, *args, **kwargs):
    #     # self.slug = slugify("{} {}".format(self.surname, self.first_name))
    #     self.slug = slugify(self.surname)
    #     super(Author, self).save(*args, **kwargs)

    def get_absolute_url_list(self):
        return reverse("verse:verse_list_by_author", args=[self.slug])

    def get_absolute_url_detail(self):
        return reverse("author:author_detail", args=[self.id, self.slug])
