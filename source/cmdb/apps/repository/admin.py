# _*_coding:utf-8_*_
__author__ = 'ChenKai'
__date__ = "2019-03"
from django.contrib import admin
from . import models

admin.site.register(models.BusinessUnit)
admin.site.register(models.IDC)
admin.site.register(models.Tag)
admin.site.register(models.Asset)
admin.site.register(models.Server)
admin.site.register(models.SecurityDevice)
admin.site.register(models.NetworkDevice)
admin.site.register(models.Software)
admin.site.register(models.CPU)
admin.site.register(models.RAM)
admin.site.register(models.Disk)
admin.site.register(models.Nic)
admin.site.register(models.AssetRecord)
admin.site.register(models.ErrorLog)
admin.site.register(models.AssetApproval)
