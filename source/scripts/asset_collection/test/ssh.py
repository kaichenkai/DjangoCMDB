# -*- coding: utf-8 -*-

import paramiko
import requests


class SSHPlugin(object):
    @classmethod
    def data_collection(cls, cmd):
        # ---------- 获取未采集主机名 ----------
        # hosts = requests.get("http://localhost/asset/hosts")
        hosts = ["192.168.0.115", "192.168.0.105"]

        # ---------- 远程操作服务器 ----------
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname="192.168.0.115", port=22, username="root", password="chenkai")
        # 执行命令
        stdin, stdout, stderr = ssh.exec_command(cmd)
        # 补充输入内容
        stdin.write("yes")
        # 获取命令结果
        result = stdout.read()
        # 关闭连接
        ssh.close()

        # ---------- 整理数据 ----------
        asset_info_dict = {
            "nic": {},
            "disk": {},
            "memory": {}
        }

        # ---------- 发送数据 ----------
        ret = requests.post("http://localhost:8000/asset/", data=asset_info_dict)
        return result
