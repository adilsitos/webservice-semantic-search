# Generated by Django 3.0.8 on 2021-07-29 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0008_auto_20210729_1405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recommendation',
            name='user_response',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'Yes')], verbose_name='Response from users'),
        ),
    ]