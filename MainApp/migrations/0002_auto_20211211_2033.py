# Generated by Django 3.0.5 on 2021-12-12 02:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Toppings',
            new_name='Topping',
        ),
        migrations.AlterModelOptions(
            name='topping',
            options={'verbose_name_plural': 'toppings'},
        ),
    ]