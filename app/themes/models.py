from django.db import models
from filebrowser.fields import FileBrowseField

from categories.models import Category
from levels.models import Level
from words.models import Word


class Theme(models.Model):
    name = models.CharField("Название темы", max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория")
    level = models.ForeignKey(Level, on_delete=models.SET_NULL, verbose_name="Уровень", null=True)
    photo = FileBrowseField(
        "Иконка темы",
        max_length=200,
        help_text="Загрузите изображение",
        directory="/media/uploads/",
        extensions=[".jpg", ".jpeg", ".gif", ".png", ".JPG", ".PNG", ".JPEG", ".GIF"],
        null=True
    )
    words = models.ManyToManyField(Word, verbose_name="Слова", blank=True)

    class Meta:
        verbose_name = "Тема"
        verbose_name_plural = "Темы"

    def __str__(self):
        return "%s| %s" % (self.id, self.name)

