# -*- coding:utf-8 -*-
import json
import importlib
from django.http import JsonResponse, HttpResponse
from repository.utils.plugin import get_untreated_servers
from repository import models
from repository import config
# django rest
from rest_framework.views import APIView


class AssetServersAPI(APIView):
    def get(self, request):
        """
        获取今日未更新的资产, 适用于agent或ssh客户端
        :param request:
        :return:
        """
        # test = {'user': '用户名', 'pwd': '密码'}
        # result = json.dumps(test,ensure_ascii=True)
        # result = json.dumps(test,ensure_ascii=False)
        # return HttpResponse(result)

        # test = {'user': '用户名', 'pwd': '密码'}
        # result = json.dumps(test,ensure_ascii=True)
        # result = json.dumps(test,ensure_ascii=False)
        # return HttpResponse(result,content_type='application/json')

        # test = {'user': '用户名', 'pwd': '密码'}
        # return JsonResponse(test, json_dumps_params={"ensure_ascii": False})
        """
        {
            "status": true,
            "message": null,
            "data": [
                {
                    "hostname": "seemmo_one"
                },
                {
                    "hostname": "seemmo_two"
                }
            ],
            "error": null
        }
        """
        response = get_untreated_servers()
        return JsonResponse(response.__dict__)

    def post(self, request):
        """
        更新或者添加资产信息
        :param request:
        :return: 1000 成功;1001 接口授权失败;1002 数据库中资产不存在
        """
        server_info = json.loads(request.body.decode("utf-8"))
        server_info = json.loads(server_info)
        hostname = server_info["hostname"]

        ret = {"code": 1000, "message": f"{hostname}更新完成"}

        # 对QuerySet使用select_related()函数后，Django会获取相应外键对应的对象
        server_obj = models.Server.objects.filter(hostname=hostname).select_related('asset').first()
        if not server_obj:
            ret["code"] = 1002
            ret["message"] = f"{hostname}资产不存在"
        else:
            for key, plugin in config.PLUGINS_DICT.items():
                # 从配置文件中读取组件类
                cls_path, cls_name = plugin.rsplit(".", 1)
                cls = getattr(importlib.import_module(cls_path), cls_name)
                response = cls.process(server_obj, server_info)
                if not response.status:
                    ret["code"] = 1003
                    ret["message"] = f"{hostname}资产变更异常"
                if hasattr(cls, "update_last_time"):
                    cls.update_last_time(server_obj)
        return JsonResponse(ret)
