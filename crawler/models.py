from django.db import models

# Create your models here.
from django_mysql.models import EnumField


class Kin(models.Model):
    keyword = models.CharField(max_length=20)
    d1id = models.CharField(max_length=10)
    dir_id = models.CharField(max_length=20)
    doc_id = models.CharField(max_length=20)
    url = models.CharField(max_length=200)
    content = models.TextField()
    use_yn = EnumField(choices=['Y', 'N'])
    created_datetime = models.DateTimeField(auto_now_add=True)
    updated_datetime = models.DateTimeField(auto_now=True)
    type = models.CharField(max_length=30, null=True)



class BadWord(models.Model):
    type = models.CharField(max_length=30)
    keyword = models.CharField(max_length=20)

    def __str__(self):
        return self.keyword