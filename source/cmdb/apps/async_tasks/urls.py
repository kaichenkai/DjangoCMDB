# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views
# rest framework
from rest_framework.routers import DefaultRouter


urlpatterns = [
    url(r"test/", views.ImageCodeAPI.as_view(), name="ImageCodeAPI"),
]

# router = DefaultRouter()
# router.register(r"test", views.ImageCodeView, base_name="test")
# urlpatterns += router.urls
