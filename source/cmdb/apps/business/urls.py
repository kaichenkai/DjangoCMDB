# -*- coding:utf-8 -*-
from django.conf.urls import url
from CMDB.apps.business import views

# rest framework
from rest_framework.routers import DefaultRouter


urlpatterns = [
    # 添加子路由
    # url(r"^books/$", views.BooksAPI.as_view(), name="BooksAPI"),
    # url(r"^book/(?P<book_id>\d+)/$", views.BookAPI.as_view(), name="BookAPI"),
    # url(r"^heros/$", views.HeroInfo.as_view(), name="HeroInfo"),
]

router = DefaultRouter()  # 可以处理视图的路由器
# router.register(r"books", views.BooksAPI, base_name="books")  # 向路由中注册视图集
# router.register(r"heros", views.HerosAPI, base_name="heros")  # 向路由中注册视图集

urlpatterns += router.urls
