# Generated by Django 3.2.4 on 2021-06-28 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authy', '0007_auto_20210628_1845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='user_statut',
            field=models.CharField(choices=[('6eme', '6eme'), ('5eme', '5eme'), ('4eme', '4eme'), ('3eme', '3eme'), ('2nde', '2nde'), ('1ere', '1ere'), ('Tle', 'Tle')], default='6eme', max_length=15),
        ),
    ]
