# Generated by Django 4.1.6 on 2023-08-12 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nza', '0006_remove_quote_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='quote',
            name='author',
            field=models.CharField(default=1, max_length=50, verbose_name='Автор:'),
            preserve_default=False,
        ),
    ]
