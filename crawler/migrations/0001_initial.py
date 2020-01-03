# Generated by Django 2.2.1 on 2019-05-08 07:44

from django.db import migrations, models
import django_mysql.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BadWord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=30)),
                ('keyword', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Kin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keyword', models.CharField(max_length=20)),
                ('d1id', models.CharField(max_length=10)),
                ('dir_id', models.CharField(max_length=20)),
                ('doc_id', models.CharField(max_length=20)),
                ('url', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('use_yn', django_mysql.models.EnumField(choices=[('Y', 'Y'), ('N', 'N')])),
                ('created_datetime', models.DateTimeField(auto_now_add=True)),
                ('updated_datetime', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=30)),
                ('role', django_mysql.models.EnumField(choices=[('INTRO', 'INTRO'), ('OUTRO', 'OUTRO'), ('COMMON', 'COMMON'), ('LEVEL1', 'LEVEL1'), ('LEVEL2', 'LEVEL2'), ('LEVEL3', 'LEVEL3')])),
                ('content', models.TextField()),
            ],
        ),
    ]
