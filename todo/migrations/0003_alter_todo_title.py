# Generated by Django 3.2 on 2022-09-26 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_alter_todo_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='title',
            field=models.CharField(blank=True, max_length=50, verbose_name='baslik'),
        ),
    ]