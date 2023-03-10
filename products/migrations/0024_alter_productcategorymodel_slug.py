# Generated by Django 3.2.18 on 2023-03-11 12:38

import autoslug.fields
from django.db import migrations
import products.models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0023_alter_productcategorymodel_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productcategorymodel',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='name', slugify=products.models.set_slugify),
        ),
    ]
