# Generated by Django 4.0.3 on 2022-04-18 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Musicy', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogentry',
            name='fecha',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
