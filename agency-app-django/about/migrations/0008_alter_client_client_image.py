# Generated by Django 3.2.4 on 2022-05-23 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0007_auto_20220523_0041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='client_image',
            field=models.ManyToManyField(blank=True, null=True, related_name='cl_img', to='about.Client_image'),
        ),
    ]
