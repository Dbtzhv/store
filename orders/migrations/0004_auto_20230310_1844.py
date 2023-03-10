# Generated by Django 3.2.18 on 2023-03-10 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20230306_1301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordermodel',
            name='order_sum',
            field=models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Сумма заказа'),
        ),
        migrations.AlterField(
            model_name='orderproductsmodel',
            name='quantity',
            field=models.IntegerField(verbose_name='Количество'),
        ),
    ]