# _*_coding:utf-8_*_
__author__ = 'ChenKai'
__date__ = "2019-03"
from django.db import models
from CMDB.apps.users.models import User


class TimeBase(models.Model):
    """基础时间表"""
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


# ------------ 业务线 ------------
class BusinessUnit(TimeBase):
    """业务线"""
    name = models.CharField(max_length=64, unique=True, verbose_name="业务线")
    remark = models.TextField(null=True, blank=True, verbose_name="备注")
    status = models.BooleanField(default=True, verbose_name="是否正常")

    # one to many
    contact = models.ForeignKey(User, null=True, on_delete=models.PROTECT, verbose_name="业务负责人")

    class Meta:
        db_table = "tb_business_unit"
        verbose_name = "业务线"
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"<{self.name}>"


# ------------- 机房 -------------
class IDC(TimeBase):
    """机房"""
    name = models.CharField(max_length=64, unique=True, verbose_name="名称")
    floor = models.IntegerField(null=True, blank=True, verbose_name="所在楼层")
    remark = models.TextField(null=True, blank=True, verbose_name="备注")
    status = models.BooleanField(default=True, verbose_name="是否启用")

    # one to many
    manager = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='机房管理员')

    class Meta:
        db_table = "tb_idc"
        verbose_name = "机房"
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"<{self.name}>"


# ------------- 标签 -------------
class Tag(TimeBase):
    """资产标签"""
    name = models.CharField(max_length=64, unique=True, verbose_name="名称")
    status = models.BooleanField(default=True, verbose_name="是否有效")

    class Meta:
        db_table = "tb_tag"
        verbose_name = "标签"
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"<{self.name}>"


# ------------ 主要资产 -----------
class Asset(TimeBase):
    """资产, 所有资产公共信息"""
    ASSET_TYPE = (
        ("server",          "服务器"),
        ("network_device",  "网络设备"),
        ("storage_device",  "存储设备"),
        ("security_device", "安全设备"),
        ("switch",          "交换机"),
        ("router",          "路由器"),
        ("parts",           "部件"),
        ("firewall",        "防火墙"),
        ("NLB",             "网络负载均衡"),
        ("wireless",        "无线AP"),
        ("software",        "软件资产"),
        ("others",          "其他资产")
    )
    ASSET_STATUS = ((0, "在线"), (1, "下架"), (2, "故障"), (3, "备用"))

    name = models.CharField(max_length=64, unique=True, verbose_name="名称")
    asset_type = models.CharField(choices=ASSET_TYPE, max_length=64, default="server", verbose_name="类型")
    status = models.SmallIntegerField(choices=ASSET_STATUS, default=0, verbose_name="状态")
    cabinet_num = models.IntegerField(null=True, blank=True, verbose_name="机柜号")
    cabinet_order = models.IntegerField(null=True, blank=True, verbose_name="机柜中序号")

    purchasing_date = models.DateField(verbose_name="购买日期")
    expore_date = models.DateField(verbose_name="过保修期")
    price = models.FloatField(verbose_name="单价")
    remark = models.TextField(null=True, blank=True, verbose_name="备注")

    # one to many
    business_unit = models.ForeignKey("BusinessUnit", null=True, blank=True, on_delete=models.PROTECT,
                                      verbose_name="所属业务线")
    idc = models.ForeignKey("IDC", null=True, blank=True, on_delete=models.PROTECT, verbose_name="IDC机房")
    creator = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name="创建人")
    # many to many
    tags = models.ManyToManyField("Tag", verbose_name="标签")

    class Meta:
        db_table = "tb_asset"
        verbose_name = "资产"
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"<{self.id}: {self.name}>"


class Server(TimeBase):
    """服务器设备"""
    SERVER_TYPE = (
        (0, "PC服务器"),
        (1, "刀片机"),
        (2, "小型机")
    )
    server_type = models.SmallIntegerField(choices=SERVER_TYPE, default=0, verbose_name="服务器类型")
    server_model = models.CharField(max_length=128, null=True, blank=True, verbose_name="服务器型号")
    hostname = models.CharField(max_length=32, unique=True, verbose_name="主机名")
    sn = models.CharField(max_length=64, unique=True, db_index=True, verbose_name="SN序列号")
    manufacturer = models.CharField(max_length=64, null=True, blank=True, verbose_name="制造商")
    manage_ip = models.GenericIPAddressField(null=True, blank=True, verbose_name="管理IP")
    os_type = models.CharField(max_length=32, null=True, blank=True, verbose_name="系统类型")
    os_version = models.CharField(max_length=32, null=True, blank=True, verbose_name="系统版本")

    cpu_count = models.IntegerField(null=True, blank=True, verbose_name="CPU核数")
    cpu_physical_count = models.IntegerField(null=True, blank=True, verbose_name="CPU物理个数")
    cpu_model = models.CharField(max_length=64, null=True, blank=True, verbose_name="CPU型号")

    # one to one
    asset = models.OneToOneField(Asset, on_delete=models.PROTECT, verbose_name="资产")
    # one to many
    creator = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name="创建人")

    class Meta:
        db_table = "tb_server"
        verbose_name = "服务器"
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"<{self.id}: {self.server_model}>"


class SecurityDevice(TimeBase):
    """安全设备"""
    DEVICE_TYPE = (
        (0, "防火墙"),
        (1, "入侵检测设备"),
        (2, "互联网网关"),
        (3, "运维审计系统")
    )

    device_type = models.SmallIntegerField(choices=DEVICE_TYPE, default=0, verbose_name="设备类型")
    model = models.CharField(max_length=128, null=True, blank=True, verbose_name="型号")

    # one to one
    asset = models.OneToOneField(Asset, on_delete=models.PROTECT, verbose_name="资产")
    # one to many
    creator = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name="创建人")

    class Meta:
        db_table = "tb_security_device"
        verbose_name = "安全设备"
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"<{self.id}: {self.device_type}>"


class NetworkDevice(TimeBase):
    """网络设备"""
    DEVICE_TYPE = (
        (0, "路由器"),
        (1, "交换机"),
        (2, "负载均衡"),
        (3, "VPN设备")
    )

    device_type = models.SmallIntegerField(choices=DEVICE_TYPE, default=0, verbose_name="设备类型")
    model = models.CharField(max_length=128, null=True, blank=True, verbose_name="型号")
    sn = models.CharField(max_length=64, unique=True, null=True, blank=True, db_index=True, verbose_name="SN序列号")
    manufacturer = models.CharField(max_length=64, null=True, blank=True, verbose_name="制造商")
    manage_ip = models.GenericIPAddressField(null=True, blank=True, verbose_name="管理IP")
    intranet_ip = models.GenericIPAddressField(null=True, blank=True, verbose_name="内网IP地址")
    port_num = models.SmallIntegerField(null=True, blank=True, verbose_name="端口数")
    device_detail = models.TextField(null=True, blank=True, verbose_name="详细配置")

    # one to one
    asset = models.OneToOneField(Asset, on_delete=models.PROTECT, verbose_name="资产")
    # one to many
    creator = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name="创建人")

    class Meta:
        db_table = "tb_network_device"
        verbose_name = "网络设备"
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"<{self.id}: {self.model}>"


class Software(TimeBase):
    """软件资产"""
    SOFTWARE_TYPE = (
        (0, "OS"),
        (1, "办公/开发软件"),
        (2, "业务软件")
    )
    LANGUAGE_TYPE = (("cn", "中文"), ("en", "英文"))

    name = models.CharField(max_length=32, null=True, blank=True, verbose_name="软件名称")
    software_type = models.SmallIntegerField(choices=SOFTWARE_TYPE, default=2, verbose_name="软件类型")
    language_type = models.CharField(max_length=32, choices=LANGUAGE_TYPE, default="cn", verbose_name="语言类型")
    version = models.CharField(max_length=32, null=True, blank=True, verbose_name="版本")
    license_num = models.IntegerField(null=True, blank=True, verbose_name="授权数量")

    # one to one
    asset = models.OneToOneField(Asset, on_delete=models.PROTECT, verbose_name="资产")
    # one to many
    creator = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name="创建人")

    class Meta:
        db_table = "tb_software"
        verbose_name = "软件资产"
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"<{self.id}: {self.name}>"


# -------------- 部件 -------------
class CPU(TimeBase):
    """CPU"""
    """server 为空时, 表示是购置的散片"""
    model = models.CharField(max_length=128, verbose_name="CPU型号")
    kernel_num = models.SmallIntegerField(null=True, blank=True, verbose_name="核数")
    manufacturer = models.CharField(max_length=64, null=True, blank=True, verbose_name="制造商")
    remark = models.TextField(null=True, blank=True, verbose_name="备注")

    # one to many
    server = models.ForeignKey(Server, null=True, blank=True, on_delete=models.PROTECT, verbose_name="服务器")

    class Meta:
        db_table = "tb_cpu"
        verbose_name = "CPU"
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"<{self.id}: {self.model}>"


class RAM(TimeBase):
    """内存"""
    """server 为空时, 表示是购置的散片"""
    slot = models.CharField(max_length=32, verbose_name="插槽位")
    model = models.CharField(max_length=128, null=True, blank=True, verbose_name="内存型号")
    sn = models.CharField(max_length=64, null=True, blank=True, verbose_name="SN号")
    capacity = models.FloatField(null=True, blank=True, verbose_name="容量(GB)")
    speed = models.CharField(max_length=64, null=True, blank=True, verbose_name="速度")
    manufacturer = models.CharField(max_length=64, null=True, blank=True, verbose_name="制造商")
    remark = models.TextField(null=True, blank=True, verbose_name="备注")

    # one to many
    server = models.ForeignKey(Server, null=True, blank=True, on_delete=models.PROTECT, verbose_name="服务器")

    class Meta:
        db_table = "tb_ram"
        verbose_name = "内存"
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"<{self.id}: {self.model}>"


class Disk(TimeBase):
    """硬盘"""
    """server 为空时, 表示是购置的散片"""
    INTERFACE_TYPE = (
        ('SATA',    'SATA'),
        ('SAS',     'SAS'),
        ('SCSI',    'SCSI'),
        ('SSD',     'SSD'),
    )

    slot = models.CharField(max_length=32, verbose_name="插槽位")
    model = models.CharField(max_length=128, null=True, blank=True, verbose_name="型号")
    pd_type = models.CharField(max_length=64, choices=INTERFACE_TYPE, verbose_name="类型")
    capacity = models.FloatField(null=True, blank=True, verbose_name="容量(GB)")
    speed = models.CharField(max_length=64, null=True, blank=True, verbose_name="速度")
    manufacturer = models.CharField(max_length=64, null=True, blank=True, verbose_name="制造商")
    remark = models.TextField(null=True, blank=True, verbose_name="备注")

    # one to many
    server = models.ForeignKey(Server, null=True, blank=True, on_delete=models.PROTECT, verbose_name="服务器")

    class Meta:
        db_table = "tb_disk"
        verbose_name = "硬盘"
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"<{self.id}: {self.model}>"


class Nic(TimeBase):
    """网卡"""
    """server 为空时, 表示是购置的散片"""
    name = models.CharField(max_length=32, verbose_name="名称")  # 例如:eth0
    model = models.CharField(max_length=128, null=True, blank=True, verbose_name="型号")
    mac_addr = models.CharField(max_length=64, null=True, blank=True, verbose_name="mac地址")
    netmask = models.GenericIPAddressField(null=True, blank=True, verbose_name="网络掩码")
    ip_addr = models.GenericIPAddressField(null=True, blank=True, verbose_name="IP地址")
    manufacturer = models.CharField(max_length=64, null=True, blank=True, verbose_name="制造商")
    up = models.BooleanField(default=False, verbose_name="运行状态")
    remark = models.TextField(null=True, blank=True, verbose_name="备注")

    # one to many
    server = models.ForeignKey(Server, null=True, blank=True, on_delete=models.PROTECT, verbose_name="服务器")

    class Meta:
        db_table = "tb_nic"
        verbose_name = "网卡"
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"<{self.id}: {self.name}>"


# ------------ 变更记录 ------------
class AssetRecord(TimeBase):
    """资产变更记录"""
    """creator 为空时, 表示是自动汇报的数据"""
    EVENT_TYPE = (
        (1, '硬件变更'),
        (2, '新增配件'),
        (3, '设备下线'),
        (4, '设备上线'),
        (5, '其他'),
    )

    record_type = models.SmallIntegerField(choices=EVENT_TYPE, default=5, verbose_name="类型")
    content = models.TextField(null=True, verbose_name="变更详情")
    remark = models.TextField(null=True, blank=True, verbose_name="备注")

    # one to many
    asset = models.ForeignKey(Asset, on_delete=models.PROTECT, verbose_name="资产")
    creator = models.ForeignKey(User, null=True, blank=True, on_delete=models.PROTECT, verbose_name="操作人")

    class Meta:
        db_table = "tb_asset_record"
        verbose_name = "资产变更记录"
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"<{self.id}: {self.asset.name}>"


class ErrorLog(TimeBase):
    """错误日志,如：agent采集数据错误 或 运行错误"""
    title = models.CharField(max_length=32)
    content = models.TextField()

    # one to many
    asset = models.ForeignKey(Asset, null=True, blank=True, on_delete=models.PROTECT, verbose_name="资产")

    class Meta:
        db_table = "tb_error_log"
        verbose_name = "错误日志"
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"<{self.id}: {self.title}>"


# ------------ 资产审批 ------------
class AssetApproval(TimeBase):
    """资产审批区"""
    ASSET_TYPE = (
        ("server",          "服务器"),
        ("network_device",  "网络设备"),
        ("storage_device",  "存储设备"),
        ("security_device", "安全设备"),
        ("switch",          "交换机"),
        ("router",          "路由器"),
        ("parts",           "部件"),
        ("firewall",        "防火墙"),
        ("NLB",             "网络负载均衡"),
        ("wireless",        "无线AP"),
        ("software",        "软件资产"),
        ("others",          "其他资产")
    )
    SPECIFICATION_TYPE = (
        (0, "台"),
        (1, "个"),
        (2, "张")
    )

    asset_type = models.CharField(choices=ASSET_TYPE, max_length=64, default="server", verbose_name="类型")
    model = models.CharField(max_length=128, null=True, blank=True, verbose_name="型号")
    manufacturer = models.CharField(max_length=64, null=True, blank=True, verbose_name="制造商")
    specification = models.SmallIntegerField(choices=SPECIFICATION_TYPE, verbose_name="规格")
    price = models.FloatField(verbose_name="单价")
    count = models.IntegerField(null=True, blank=True, verbose_name="申请数量")
    application_date = models.DateField(verbose_name="申请日期")
    approved = models.BooleanField(default=False, verbose_name="是否批准")
    approved_date = models.DateField(null=True, blank=True, verbose_name="批准日期")
    remark = models.TextField(null=True, blank=True, verbose_name="备注")

    # one to many
    approved_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.PROTECT, verbose_name="批准人")

    class Meta:
        db_table = "tb_asset_approval"
        verbose_name = "审批记录"
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"<{self.id}: {self.asset_type}>"
