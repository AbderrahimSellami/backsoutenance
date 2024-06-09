# Generated by Django 5.0.4 on 2024-06-06 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('utilisateurs', '0003_delete_admins_delete_enseignants_delete_etudiants'),
    ]

    operations = [
        migrations.CreateModel(
            name='Utilisateurs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Utilisateur', models.CharField(max_length=256)),
                ('Login', models.CharField(max_length=128)),
                ('MDP', models.CharField(max_length=64)),
            ],
        ),
    ]
