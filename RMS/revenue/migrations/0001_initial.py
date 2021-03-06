# Generated by Django 3.2.5 on 2021-07-24 09:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='Revenue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoice_amount_euro', models.DecimalField(decimal_places=2, max_digits=6)),
                ('transaction_date', models.DateField()),
                ('revenue_charged_euro', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
                ('cost_of_goods_euro', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
                ('account_invoice_received', models.PositiveIntegerField()),
                ('revenue_account_name', models.CharField(default=111001, max_length=50)),
                ('operational_costs_euro', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='revenue.customer')),
            ],
        ),
    ]
