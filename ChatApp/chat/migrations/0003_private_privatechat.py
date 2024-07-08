# Generated by Django 5.0.6 on 2024-07-07 06:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_chat_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='private',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('u_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='privateChat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=10000)),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('u_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chat.private')),
            ],
        ),
    ]
