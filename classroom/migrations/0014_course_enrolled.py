# Generated by Django 3.2.4 on 2021-06-28 15:12

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('classroom', '0013_remove_course_enrolled'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='enrolled',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
