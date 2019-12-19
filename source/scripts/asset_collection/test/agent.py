# -*- coding: utf-8 -*-

import subprocess
import requests


class AgentPlugin(object):
    @classmethod
    def data_collection(cls, cmd):
        # ---------- 数据采集 ----------
        result = subprocess.getoutput(cmd)
        # 使用正则处理result

        # ---------- 整理数据 ----------
        asset_info_dict = {
            "nic": {},
            "disk": {},
            "memory": {}
        }

        # ---------- 发送数据 ----------
        ret = requests.post("http://localhost:8000/asset/", data=asset_info_dict)
        return ret
