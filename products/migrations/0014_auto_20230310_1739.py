# Generated by Django 3.2.18 on 2023-03-10 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_auto_20230310_1705'),
    ]

    operations = [
        migrations.CreateModel(
            name='ParameterModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Название')),
                ('value', models.CharField(max_length=255, verbose_name='Значение')),
            ],
            options={
                'verbose_name': 'Параметр',
                'verbose_name_plural': 'Параметры',
            },
        ),
        migrations.AddField(
            model_name='productmodel',
            name='parameter',
            field=models.ManyToManyField(to='products.ParameterModel', verbose_name='Продукт'),
        ),
    ]