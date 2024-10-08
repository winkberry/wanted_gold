# Generated by Django 5.1 on 2024-09-11 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.CharField(max_length=20, unique=True)),
                ('order_date', models.DateTimeField(auto_now_add=True)),
                ('customer_name', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('ORDER_COMPLETE', '주문 완료'), ('PAYMENT_COMPLETE', '입금 완료'), ('SHIPPED', '발송 완료'), ('RECEIVED', '수령 완료')], default='ORDER_COMPLETE', max_length=20)),
                ('order_type', models.CharField(choices=[('BUY', '구매'), ('SELL', '판매')], max_length=4)),
                ('product', models.CharField(max_length=50)),
                ('quantity', models.DecimalField(decimal_places=2, max_digits=10)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=12)),
                ('shipping_address', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
