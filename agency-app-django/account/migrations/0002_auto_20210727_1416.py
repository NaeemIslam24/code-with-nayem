# Generated by Django 3.2.4 on 2021-07-27 14:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, default='user/user.png', null=True, upload_to='user'),
        ),
        migrations.CreateModel(
            name='SubTest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district', models.CharField(max_length=25)),
                ('user1', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='account.test')),
            ],
        ),
    ]
