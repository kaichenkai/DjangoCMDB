# -*- coding: utf-8 -*-
from conf import settings
from src.client import AgentClient, SSHClient


def run():
    if settings.MODE == "agent":
        client = AgentClient()
    elif settings.MODE == "ssh":
        client = SSHClient()
    else:
        raise Exception("配置采集模式错误: settings.MODE")

    client.process()
