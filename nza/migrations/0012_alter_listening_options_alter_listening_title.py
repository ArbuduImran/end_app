# Generated by Django 4.1.6 on 2023-08-12 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nza', '0011_alter_question_answer_1_alter_question_answer_2_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='listening',
            options={'verbose_name': 'Аудирование', 'verbose_name_plural': 'Аудирование'},
        ),
        migrations.AlterField(
            model_name='listening',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Аудирование'),
        ),
    ]