# Generated by Django 3.1.7 on 2021-04-14 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('text', models.TextField(max_length=400)),
                ('img', models.ImageField(upload_to='')),
                ('title2', models.CharField(max_length=100)),
                ('html', models.TextField(max_length=4)),
                ('css', models.TextField(max_length=4)),
                ('javascript', models.TextField(max_length=4)),
                ('photoshop', models.TextField(max_length=4)),
            ],
        ),
    ]
