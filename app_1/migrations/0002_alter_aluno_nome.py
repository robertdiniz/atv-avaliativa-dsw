# Generated by Django 4.2.6 on 2023-10-26 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='nome',
            field=models.CharField(max_length=50, verbose_name='Nome'),
        ),
    ]
