# Generated by Django 3.1.7 on 2021-04-15 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Top_header',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fav_icon', models.ImageField(upload_to='')),
                ('fav_icon2', models.ImageField(upload_to='')),
                ('number', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('twitter', models.URLField()),
                ('facebook', models.URLField()),
                ('instagram', models.URLField()),
                ('linkedin', models.URLField()),
            ],
        ),
    ]