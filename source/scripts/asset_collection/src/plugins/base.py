# -*- coding: utf-8 -*-
from conf import settings
from lib.logger import Logger


class BasePlugin(object):
    def __init__(self, hostname=""):
        self.test_mode = settings.TEST_MODE
        self.mode_list = ["agent", "ssh", "salt"]
        self.os_list = ["ubuntu", "centos"]
        self.hostname = hostname
        # 默认采集模式 and 被采集服务器默认操作系统
        if hasattr(settings, "MODE") and hasattr(settings, "OS_TYPE"):
            self.mode = settings.MODE
            self.os_type = settings.OS_TYPE
        else:
            self.mode = "agent"
            self.os_type = "ubuntu"
        self.logger = Logger()

    def exec_shell_cmd(self, cmd):
        # 根据模式进行相应操作
        if settings.MODE not in self.mode_list:
            raise Exception(f"configuration info error:{settings.MODE}")
        func = getattr(self, self.mode)
        output = func(cmd)
        return output

    def agent(self, cmd):
        import subprocess

        output = subprocess.getoutput(cmd)
        return output

    def ssh(self, cmd):
        import paramiko

        private_key = paramiko.RSAKey.from_private_key_file(settings.SSH_PRIVATE_KEY)
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=self.hostname, port=settings.SSH_PORT, username=settings.SSH_USER, pkey=private_key)
        stdin, stdout, stderr = ssh.exec_command(cmd)
        result = stdout.read()
        ssh.close()
        return result

    def execute(self):
        if settings.OS_TYPE not in self.os_list:
            raise Exception(f"configuration info error:{settings.OS_TYPE}")
        func = getattr(self, self.os_type)
        return func()

    def ubuntu(self):
        """
        子类需要重写此方法，用于获取ubuntu系统的资产信息
        :return:
        """
        raise NotImplementedError("you must implement ubuntu method")

    def centos(self):
        """
        子类需要重写此方法，用于获取centos系统的资产信息
        :return:
        """
        raise NotImplementedError("you must implement centos method")
