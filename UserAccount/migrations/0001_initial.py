# Generated by Django 3.1.5 on 2021-02-02 06:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('mobile', models.CharField(max_length=10)),
                ('pan', models.CharField(max_length=10, unique=True)),
                ('total_number_of_accounts', models.IntegerField()),
                ('credit_score', models.IntegerField()),
                ('address', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_no', models.CharField(max_length=50)),
                ('amount_overdue', models.FloatField()),
                ('current_balance', models.FloatField()),
                ('date_opened', models.DateField()),
                ('date_reported', models.DateField()),
                ('lender', models.CharField(max_length=50)),
                ('sanction_amount', models.FloatField()),
                ('type', models.CharField(max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UserAccount.user')),
            ],
        ),
    ]
