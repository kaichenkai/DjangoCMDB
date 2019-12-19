# _*_coding:utf-8_*_
__author__ = 'ChenKai'
__date__ = "2019-03"
from django.contrib import admin
from . import models

admin.site.register(models.User)
