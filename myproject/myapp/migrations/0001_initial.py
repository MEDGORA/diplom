# Generated by Django 5.0.2 on 2024-03-05 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Invocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('second_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('address', models.TextField()),
                ('description', models.TextField()),
                ('personal_account', models.CharField(max_length=50)),
                ('date_created_personal', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='New',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('foto_of_new', models.ImageField(upload_to='templates/myapp/images')),
                ('date_created_new', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Personal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('second_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('foto_of_personal', models.ImageField(upload_to='')),
                ('post', models.CharField(max_length=200)),
                ('date_created_personal', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profession', models.CharField(max_length=100)),
                ('requirements', models.TextField()),
                ('description', models.TextField()),
                ('date_created_new', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Сonsumer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('second_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('address', models.TextField()),
                ('personal_account', models.CharField(max_length=50)),
                ('date_created_personal', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
