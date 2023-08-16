# Generated by Django 4.1.6 on 2023-08-15 10:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Antonym',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=100)),
                ('antonyms', models.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=100, verbose_name='Категории:')),
            ],
            options={
                'verbose_name': 'Категории',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chapter', models.CharField(max_length=255, verbose_name='Раздел')),
            ],
            options={
                'verbose_name': 'Раздел',
                'verbose_name_plural': 'Раздел',
            },
        ),
        migrations.CreateModel(
            name='Idiom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=255, verbose_name='Введите идиому')),
            ],
            options={
                'verbose_name': 'Идиомы',
                'verbose_name_plural': 'Идиомы',
            },
        ),
        migrations.CreateModel(
            name='Listening',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Аудирование')),
                ('text', models.TextField(verbose_name='Текст')),
            ],
            options={
                'verbose_name': 'Аудирование',
                'verbose_name_plural': 'Аудирование',
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keyword', models.CharField(max_length=100, verbose_name='Введите слово:')),
                ('image_url', models.URLField(verbose_name='Ссылка на фото:')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Фото',
                'verbose_name_plural': 'Фото',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=255, verbose_name='Текст:')),
                ('answer_1', models.CharField(max_length=100, verbose_name='Ответ 1:')),
                ('answer_2', models.CharField(max_length=100, verbose_name='Ответ 2:')),
                ('answer_3', models.CharField(max_length=100, verbose_name='Ответ 3:')),
                ('answer_4', models.CharField(max_length=100, verbose_name='Ответ 4:')),
                ('correct_answer_index', models.PositiveSmallIntegerField(choices=[(1, 'Answer 1'), (2, 'Answer 2'), (3, 'Answer 3'), (4, 'Answer 4')], verbose_name='Правильный ответ:')),
            ],
            options={
                'verbose_name': 'Tест',
                'verbose_name_plural': 'Тест',
            },
        ),
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=255, verbose_name='Введите цитату:')),
                ('author', models.TextField(max_length=50, verbose_name='Автор:')),
            ],
            options={
                'verbose_name': 'Цитаты',
                'verbose_name_plural': 'Цитаты',
            },
        ),
        migrations.CreateModel(
            name='Subsection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subsection', models.CharField(max_length=255, verbose_name='Подраздел')),
            ],
            options={
                'verbose_name': 'Подраздел',
                'verbose_name_plural': 'Подраздел',
            },
        ),
        migrations.CreateModel(
            name='Synonym',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=100)),
                ('synonym', models.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=100, verbose_name='Слово')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nza.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Слова',
                'verbose_name_plural': 'Слова',
            },
        ),
        migrations.CreateModel(
            name='Grammar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Введите тему:')),
                ('description', models.TextField(verbose_name='Введите описание темы:')),
                ('chapter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nza.chapter', verbose_name='Раздел')),
                ('subsection', models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='nza.subsection', verbose_name='Подраздел')),
                ('test', models.ManyToManyField(to='nza.question')),
            ],
            options={
                'verbose_name': 'Грамматика',
                'verbose_name_plural': 'Грамматика',
            },
        ),
    ]
