# Generated by Django 5.0.6 on 2024-07-08 05:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0004_rename_u_name_private_user_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='privatechat',
            name='user',
        ),
        migrations.DeleteModel(
            name='private',
        ),
        migrations.DeleteModel(
            name='privateChat',
        ),
    ]
