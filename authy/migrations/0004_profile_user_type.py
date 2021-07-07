# Generated by Django 3.0.6 on 2021-06-21 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authy', '0003_remove_profile_user_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='user_type',
            field=models.CharField(choices=[('teacher', 'teacher'), ('student', 'student'), ('parent', 'parent')], default='student', max_length=10),
        ),
    ]
