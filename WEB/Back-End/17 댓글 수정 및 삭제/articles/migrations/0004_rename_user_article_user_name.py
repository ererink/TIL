# Generated by Django 3.2.13 on 2022-10-19 01:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_article_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='user',
            new_name='user_name',
        ),
    ]
