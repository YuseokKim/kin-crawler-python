# Generated by Django 2.2.1 on 2019-05-12 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crawler', '0005_auto_20190510_0839'),
    ]

    operations = [
        migrations.AddField(
            model_name='reply',
            name='comment',
            field=models.CharField(max_length=100, null=True),
        ),
    ]