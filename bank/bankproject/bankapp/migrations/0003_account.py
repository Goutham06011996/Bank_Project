# Generated by Django 4.2 on 2023-04-27 09:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bankapp', '0002_delete_account'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('date', models.DateField()),
                ('gender', models.CharField(max_length=10)),
                ('phone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=200)),
                ('account_type', models.CharField(max_length=20)),
                ('debit_card', models.BooleanField()),
                ('credit_card', models.BooleanField()),
                ('cheque_book', models.BooleanField()),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bankapp.branch')),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bankapp.district')),
            ],
        ),
    ]
