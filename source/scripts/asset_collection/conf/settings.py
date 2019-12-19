# -*- coding: utf-8 -*-
import os
BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# -------------------------------------
# ------------ 1、数据采集 -------------
# -------------------------------------
# 是否测试模式，测试模时候数据从files目录下读取
TEST_MODE = True

# 采集资产的方式，选项有：agent(默认), salt, ssh
MODE = 'ssh'

# 如果采用SSH方式，则需要配置SSH的KEY和USER
SSH_PRIVATE_KEY = "/home/auto/.ssh/id_rsa"
SSH_USER = "seemmo"
SSH_PORT = 22

# 被采集主机操作系统类型
OS_TYPE = "ubuntu"

# Agent模式保存服务器唯一ID的文件
CERT_FILE_PATH = os.path.join(BASEDIR, 'config', 'cert')

# 采集硬件数据的插件
PLUGINS_DICT = {
    'cpu': 'src.plugins.cpu.CpuPlugin',
    'disk': 'src.plugins.disk.DiskPlugin',
    'main_board': 'src.plugins.main_board.MainBoardPlugin',
    'memory': 'src.plugins.memory.MemoryPlugin',
    'nic': 'src.plugins.nic.NicPlugin',
}


# ------------------------------------
# ------------ 2、数据推送 ------------
# ------------------------------------
# 用于API认证的KEY
KEY = '299095cc-1330-11e5-b06a-a45e60bec08b'
# 用于API认证的请求头
AUTH_KEY_NAME = 'auth-key'


# 资产信息API
ASSET_API = "http://10.10.19.250:8000/repository/asset/servers/"
"""
POST时，返回值：{'code': xx, 'message': 'xx'}
 code:
    - 1000 成功;
    - 1001 接口授权失败;
    - 1002 数据库中资产不存在
"""


# ------------------------------------
# -------------- 3、日志 --------------
# ------------------------------------
# 错误日志 and 运行日志
# ERROR_LOG_FILE = os.path.join("~/logs/asset_collection", 'error.log')
# INFO_LOG_FILE = os.path.join("~/logs/asset_collection", 'info.log')
ERROR_LOG_FILE = os.path.join(BASEDIR, "logs", "error.log")
INFO_LOG_FILE = os.path.join(BASEDIR, "logs", "info.log")
