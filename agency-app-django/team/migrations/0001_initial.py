# Generated by Django 3.1.7 on 2021-04-15 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='team/')),
                ('name', models.CharField(max_length=20)),
                ('title', models.CharField(max_length=20)),
                ('text', models.TextField(max_length=264)),
                ('twitter', models.URLField()),
                ('facebook', models.URLField()),
                ('instagram', models.URLField()),
                ('linkedin', models.URLField()),
            ],
        ),
    ]
