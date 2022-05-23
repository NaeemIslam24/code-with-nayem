# Generated by Django 3.2.4 on 2022-04-11 22:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pricing', '0003_rename_mobile_banking_name_purchasing_banking_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banking_name',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('banking_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='purchasing',
            name='banking_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='pricing.banking_name'),
        ),
    ]