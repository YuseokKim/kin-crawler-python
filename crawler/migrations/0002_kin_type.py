# Generated by Django 2.2.1 on 2019-05-08 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crawler', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='kin',
            name='type',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
