# Generated by Django 4.1.6 on 2023-08-12 08:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nza', '0004_alter_question_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subsection',
            old_name='chapter',
            new_name='subsection',
        ),
    ]