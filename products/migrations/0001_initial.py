# Generated by Django 3.2.18 on 2023-03-01 08:08

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductModel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=82)),
                ('category', models.CharField(max_length=82)),
                ('description', models.TextField(max_length=256)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('general_quantity', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Product',
            },
        ),
    ]
