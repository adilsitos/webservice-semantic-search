# Generated by Django 3.0.8 on 2021-07-28 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0004_auto_20210728_0044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recommendation',
            name='users_response',
            field=models.BooleanField(default=False, verbose_name='Response from users'),
        ),
    ]