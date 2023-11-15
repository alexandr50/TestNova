from django.db import models


class File(models.Model):
    name = models.CharField(max_length=30, verbose_name='назввние')
    data = models.TextField(verbose_name='содержимое')
