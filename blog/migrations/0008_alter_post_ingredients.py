# Generated by Django 3.2.23 on 2023-11-10 18:05

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_remove_post_is_draft'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='ingredients',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
