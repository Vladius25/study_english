from django.db import models
from filebrowser.fields import FileBrowseField


class Category(models.Model):
    name = models.CharField("Название категории", max_length=100)
    icon = FileBrowseField(
        "Иконка категории",
        max_length=200,
        help_text="Загружайте изображения в формате 4:3 или 16:9,"
                  " Размер изображения должен быть более 720 пикселей в высоту",
        directory="/media/uploads/",
        extensions=[".jpg", ".jpeg", ".gif", ".png", ".JPG", ".PNG", ".JPEG", ".GIF"],
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return "%s| %s" % (self.id, self.name)