# Generated by Django 4.1.4 on 2023-01-12 16:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_country_alter_author_country'),
    ]

    operations = [
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Тип одежды')),
            ],
        ),
        migrations.CreateModel(
            name='Clothes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=255, verbose_name='Цвет')),
                ('season', models.CharField(choices=[('z', 'Зима'), ('l', 'Лето'), ('m', 'Демисезонная')], max_length=100, verbose_name='Сезон')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.type')),
            ],
        ),
    ]