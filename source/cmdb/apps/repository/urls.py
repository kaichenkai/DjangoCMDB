# -*- coding:utf-8 -*-
from django.conf.urls import url
from repository.views import servers

urlpatterns = [
    url(r"^asset/servers/$", servers.AssetServersAPI.as_view(), name="AssetServersAPI"),
]
