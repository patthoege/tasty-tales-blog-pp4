# Generated by Django 3.2.22 on 2023-10-27 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20231026_1000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='cooking_time',
            field=models.DurationField(),
        ),
        migrations.AlterField(
            model_name='post',
            name='preparation_time',
            field=models.DurationField(),
        ),
    ]