# Generated by Django 4.0.3 on 2022-03-26 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='baslik')),
                ('completed', models.BooleanField(verbose_name='Durum')),
            ],
        ),
    ]
