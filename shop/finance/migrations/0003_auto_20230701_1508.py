# Generated by Django 3.2 on 2023-07-01 11:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('purchase', '0002_purchase_quantity'),
        ('finance', '0002_payment_purchase'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='purchase',
        ),
        migrations.CreateModel(
            name='paypu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='purschases', to='finance.payment')),
                ('purchase', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='payments', to='purchase.purchase')),
            ],
        ),
    ]
