# Generated by Django 3.1.7 on 2021-04-13 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0004_about'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=264)),
                ('url', models.URLField(max_length=264)),
                ('text', models.TextField(max_length=500)),
            ],
        ),
    ]
