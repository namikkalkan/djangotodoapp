# Generated by Django 3.2 on 2022-09-26 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_alter_todo_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='title',
            field=models.CharField(max_length=50, null=True, verbose_name='baslik'),
        ),
    ]