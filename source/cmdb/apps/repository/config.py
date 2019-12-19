# -*- coding:utf-8 -*-

# 配置需要收集的资产
PLUGINS_DICT = {
    'packages': "repository.utils.plugin.HandleBasic",
    'nic': "repository.utils.plugin.HandleNic",
    'memory': "repository.utils.plugin.HandleMemory",
    'disk': "repository.utils.plugin.HandleDisk"
}

# 资产变更类型
HARDWARE_CHANGE = 1     # 硬件变更
ADD_PARTS = 2           # 新增配件
DEVICE_OFFLINE = 3      # 设备下线
DEVICE_ONLINE = 4       # 设备上线
ASSET_REPORT = 6        # 设备上线
OTHER = 6               # 其它
