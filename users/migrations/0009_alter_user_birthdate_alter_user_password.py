# Generated by Django 4.0.3 on 2022-03-19 19:38

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_user_delete_users'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='birthdate',
            field=models.CharField(max_length=10, validators=[django.core.validators.MinLengthValidator(4)]),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(default='CfTwWaQpYsnnWrted4VANrhNNEsupb', max_length=30),
        ),
    ]
