# Generated by Django 3.0.8 on 2020-08-02 16:00

from django.db import migrations, models
import filebrowser.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Слово')),
                ('translation', models.CharField(max_length=100, verbose_name='Перевод')),
                ('transcription', models.CharField(max_length=100, verbose_name='Транскрипция')),
                ('example', models.TextField(max_length=255, verbose_name='Пример употребления')),
                ('sound', filebrowser.fields.FileBrowseField(max_length=200, null=True, verbose_name='Произношение')),
            ],
            options={
                'verbose_name': 'Слово',
                'verbose_name_plural': 'Слова',
            },
        ),
    ]
