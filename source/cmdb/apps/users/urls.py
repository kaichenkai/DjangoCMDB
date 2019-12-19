from django.conf.urls import url
from . import views

urlpatterns = [
    # 添加子路由
    url(r"index/", views.index),
]
