# Generated by Django 5.0.4 on 2024-06-10 11:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('utilisateurs', '0006_rename_date_fin_soutenance_heure'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='soutenance',
            name='heure',
        ),
    ]
