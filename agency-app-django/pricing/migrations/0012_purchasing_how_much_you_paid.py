# Generated by Django 3.2.4 on 2022-04-12 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pricing', '0011_rename_name_purchasing_user_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchasing',
            name='How_much_you_paid',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
