# Generated by Django 4.2.1 on 2024-04-23 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='utilisateurs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Utilisateur', models.CharField(max_length=256)),
                ('Login', models.CharField(max_length=128)),
                ('MDP', models.CharField(max_length=64)),
            ],
        ),
    ]
