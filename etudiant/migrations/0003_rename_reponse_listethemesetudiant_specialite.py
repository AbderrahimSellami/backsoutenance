# Generated by Django 5.0.4 on 2024-05-13 17:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('etudiant', '0002_rename_listethemes_listethemesetudiant'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listethemesetudiant',
            old_name='Reponse',
            new_name='Specialite',
        ),
    ]