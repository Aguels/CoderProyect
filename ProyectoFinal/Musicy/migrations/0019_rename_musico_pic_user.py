# Generated by Django 4.0.3 on 2022-04-19 03:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Musicy', '0018_alter_pic_musico'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pic',
            old_name='Musico',
            new_name='user',
        ),
    ]
