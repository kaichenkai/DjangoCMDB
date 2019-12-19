# _*_coding:utf-8_*_
__author__ = 'ChenKai'
__date__ = "2019-03"
from django.contrib.auth.models import AbstractUser
from django.db import models


class TimeBase(models.Model):
    """基础时间表"""
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


# --------- 用户 分组 权限 ---------
# 使用 django 自带用户模型类,
class User(AbstractUser):
    """用户表"""

    # 赠送字段
    """
    | Field        | Type         | Null | Key | Default | Extra          | detail     
    +--------------+--------------+------+-----+---------+----------------+
    | id           | int(11)      | NO   | PRI | NULL    | auto_increment | ID
    | username     | varchar(150) | NO   | UNI | NULL    |                | 用户名
    | first_name   | varchar(30)  | NO   |     | NULL    |                | 名
    | last_name    | varchar(150) | NO   |     | NULL    |                | 姓
    | password     | varchar(128) | NO   |     | NULL    |                | 密码哈希值
    | email        | varchar(254) | NO   |     | NULL    |                | 邮箱地址
    | is_staff     | tinyint(1)   | NO   |     | NULL    |                | 是否可以访问Admin 站点
    | is_active    | tinyint(1)   | NO   |     | NULL    |                | 账号是否激活
    | is_superuser | tinyint(1)   | NO   |     | NULL    |                | 是否超管   
    | last_login   | datetime(6)  | YES  |     | NULL    |                | 最后登录时间      
    | date_joined  | datetime(6)  | NO   |     | NULL    |                | 账户创建时间 

    | groups            | int(11) | NO   |  FK | NULL    |                | 与 Group 模型之间的多对多关系
    | user_permissions  | int(11) | NO   |  FK | NULL    |                | 与 Permission 模型之间的多对多关系
    """
    # 补充字段
    mobile = models.CharField(max_length=11, unique=True, null=True, blank=True, verbose_name='手机号')
    # 赠送方法
    "def set_password"  # 设置密码
    "def check_password"  # 检验密码

    class Meta:
        db_table = "tb_users"
        verbose_name = "用户"
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"<name:{self.username}>"
