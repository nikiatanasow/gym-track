# Generated by Django 3.1.1 on 2020-10-12 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercise',
            name='bodypart',
            field=models.CharField(choices=[('CO', 'Core'), ('AR', 'Arms'), ('BA', 'Back'), ('CH', 'Chest'), ('LE', 'Legs'), ('SH', 'Shoulders'), ('OT', 'Other'), ('FB', 'Full Body'), ('CA', 'Cardio')], default='CO', max_length=2),
        ),
        migrations.AddField(
            model_name='exercise',
            name='category',
            field=models.CharField(choices=[('BR', 'Barbel'), ('DM', 'Dumbbell'), ('MA', 'Machine'), ('CA', 'Cardio'), ('WB', 'Weighted Bodyweight')], default='BR', max_length=2),
        ),
    ]
