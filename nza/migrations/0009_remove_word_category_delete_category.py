# Generated by Django 4.1.6 on 2023-08-12 10:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nza', '0008_alter_quote_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='word',
            name='category',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]