from django.db import models


class Level(models.Model):
    name = models.CharField("Название", max_length=100)
    code = models.CharField("Обозначение", max_length=100)

    class Meta:
        verbose_name = "Уровень"
        verbose_name_plural = "Уровни"

    def __str__(self):
        return self.name
