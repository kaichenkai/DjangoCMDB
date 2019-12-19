# -*- coding: utf-8 -*-
from django_redis import get_redis_connection
from django.http import HttpResponse
# rest framework
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
# local
from . import constants


class ImageCodeAPI(APIView):
    """图片验证码"""
    def get(self, request):
        """
        获取验证码
        :param request:
        :param image_code_id:
        :return:
        """
        image_code_id = 1
        image = 2
        redis_conn = get_redis_connection("verify_codes")
        redis_conn.setex(f"img_{image_code_id}", constants.IMAGE_CODE_REDIS_EXPIRES, text)

        return HttpResponse(content=image, content_type="images/jpg")

    def post(self, request):
        """
        测试异步任务
        :param request:
        :return:
        """

        from source.celery_tasks.test_async_task import tasks
        print("开始调用异步任务")
        tasks.test_action.delay("test")
        print("异步任务调用完成")
        return HttpResponse(content="async task accomplish")
