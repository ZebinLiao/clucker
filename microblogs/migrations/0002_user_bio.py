# Generated by Django 3.2.8 on 2021-10-06 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('microblogs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='bio',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]