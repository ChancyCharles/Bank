# Generated by Django 5.0.7 on 2024-07-22 09:57

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('dob', models.DateField()),
                ('age', models.IntegerField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('phone_number', models.CharField(max_length=15)),
                ('mail_id', models.EmailField(max_length=254)),
                ('address', models.TextField()),
                ('district', models.CharField(choices=[('Ernakulam', 'Ernakulam'), ('Kottayam', 'Kottayam'), ('Thrissur', 'Thrissur'), ('Idukki', 'Idukki'), ('Alappuzha', 'Alappuzha')], max_length=20)),
                ('branch', models.CharField(max_length=100)),
                ('account_type', models.CharField(choices=[('Savings', 'Savings Account'), ('Current', 'Current Account')], max_length=20)),
                ('materials', models.CharField(max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Branch',
        ),
        migrations.DeleteModel(
            name='District',
        ),
    ]
