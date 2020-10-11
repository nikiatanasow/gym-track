# Generated by Django 3.1.1 on 2020-10-11 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0001_initial'),
        ('routines', '0002_routine_exercises'),
    ]

    operations = [
        migrations.AlterField(
            model_name='routine',
            name='exercises',
            field=models.ManyToManyField(blank=True, related_name='routines', to='exercises.Exercise'),
        ),
    ]
