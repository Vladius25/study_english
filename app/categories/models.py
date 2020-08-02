from django.db import models
from filebrowser.fields import FileBrowseField


class Category(models.Model):
    name = models.CharField("Название категории", max_length=100)
    icon = FileBrowseField(
        "Иконка категории",
        max_length=200,
        help_text="Загрузите изображение",
        directory="/media/uploads/",
        extensions=[".jpg", ".jpeg", ".gif", ".png", ".JPG", ".PNG", ".JPEG", ".GIF"],
        null=True
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return "%s| %s" % (self.id, self.name)
