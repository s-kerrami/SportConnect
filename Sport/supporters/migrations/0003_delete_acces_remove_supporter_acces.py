# Generated by Django 5.0.4 on 2024-04-26 13:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('supporters', '0002_acces'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Acces',
        ),
        migrations.RemoveField(
            model_name='supporter',
            name='acces',
        ),
    ]
