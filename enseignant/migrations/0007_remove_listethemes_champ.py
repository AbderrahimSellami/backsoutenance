# Generated by Django 5.0.4 on 2024-05-13 09:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('enseignant', '0006_rename_num_listethemes_id_listethemes_champ'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listethemes',
            name='Champ',
        ),
    ]
