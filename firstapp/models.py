from django.db import models


class BandMembers(models.Model):
    full_name = models.CharField(max_length=50, null=False)
    nick_name = models.CharField(max_length=10, null=False)
    password = models.CharField(max_length=50, null=False)
