# Generated by Django 5.0.4 on 2024-05-13 09:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('enseignant', '0002_listethemes'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listethemes',
            old_name='Theme',
            new_name='test',
        ),
    ]
