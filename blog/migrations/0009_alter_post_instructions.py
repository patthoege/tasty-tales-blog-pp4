# Generated by Django 3.2.23 on 2023-11-10 18:06

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_alter_post_ingredients'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='instructions',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]