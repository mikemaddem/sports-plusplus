from django.db import models


class StaticInfo(models.Model):
    about = models.TextField(default='about us')
    twitter = models.URLField(max_length=255, default='https://www.twitter.com')
    facebook = models.URLField(max_length=255, default='https://www.facebook.com')
    tos = models.TextField(default='tos')
    privacy = models.TextField(default='privacy')

