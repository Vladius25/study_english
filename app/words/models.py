from django.db import models
from filebrowser.fields import FileBrowseField


class Word(models.Model):
    name = models.CharField("Слово", max_length=100)
    translation = models.CharField("Перевод", max_length=100)
    transcription = models.CharField("Транскрипция", max_length=100)
    example = models.TextField("Пример употребления", max_length=255)
    sound = FileBrowseField(
        "Произношение",
        max_length=200,
        directory="/media/uploads/",
        extensions=[".mp3", ".wav", ".aiff", ".midi", ".m4p"],
        null=True
    )

    class Meta:
        verbose_name = "Слово"
        verbose_name_plural = "Слова"

    def __str__(self):
        return self.name
