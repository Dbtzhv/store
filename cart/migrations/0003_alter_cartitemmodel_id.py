# Generated by Django 3.2.18 on 2023-03-06 08:34

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_alter_cartmodel_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitemmodel',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
