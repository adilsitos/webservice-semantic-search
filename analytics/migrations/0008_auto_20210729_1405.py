# Generated by Django 3.0.8 on 2021-07-29 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0007_auto_20210729_1403'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recommendation',
            name='user_response',
            field=models.IntegerField(choices=[(0, 'Yes'), (1, 'No')], verbose_name='Response from users'),
        ),
    ]
