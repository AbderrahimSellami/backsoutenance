# Generated by Django 5.0.4 on 2024-06-09 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planning', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plateforme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date_debut', models.DateTimeField()),
                ('Date_fin', models.DateTimeField()),
                ('heure_debut', models.TimeField()),
                ('heure_fin', models.TimeField()),
                ('duree', models.TimeField()),
                ('salle', models.CharField(max_length=64)),
            ],
        ),
    ]
