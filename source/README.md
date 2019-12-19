# seemmo_cmdb

##### 基于 Python Django web框架，MTV架构，restfull 接口设计

##### 数据库：mysql,  redis(session存储, broker)

├── celery_tasks                                                    	异步任务模块                  
│   ├── __init__.py
│   ├── main.py
│   └── test_async_task                                        	异步任务实现
├── cmdb
│   ├── apps						子应用																
│   │   ├── repository				资产管理模块
│   │   │   ├── admin.py
│   │   │   ├── apps.py
│   │   │   ├── config.py					 	子应用配置
│   │   │   ├── http_requests					接口调试
│   │   │   ├── __init__.py
│   │   │   ├── migrations						数据库迁移
│   │   │   ├── models.py						数据库模型类(ORM)
│   │   │   ├── serializers.py					序列化器
│   │   │   ├── tests.py							单元测试
│   │   │   ├── urls.py							子应用路由
│   │   │   ├── utils							子应用工具包
│   │   │   └── views.py						子应用视图(API)
│   │   └── users					用户模块(同上)	
│   │       ├── admin.py
│   │       ├── apps.py
│   │       ├── __init__.py
│   │       ├── migrations
│   │       ├── models.py
│   │       ├── tests.py
│   │       ├── urls.py
│   │       └── views.py
│   ├── __init__.py
│   ├── libs						第三方库				
│   ├── settings					配置文件
│   │   ├── dev.py								开发环境
│   │   ├── prod.py							生产环境
│   ├── static_files				静态文件目录
│   │   └── index.html
│   ├── templates				模板文件目录
│   │   └── form.html
│   ├── urls.py					总路由
│   ├── utils						工具包(公用类和函数)
│   └── wsgi.py					
├── logs						日志目录
├── manage.py					项目启动文件
├── README.md			
├── requirements.txt	
└── scripts						脚本目录
    └── asset_collection			自动收集资产
        ├── bin
        │   └── auto_client.py
        ├── conf
        │   ├── cert
        │   ├── __pycache__
        │   │   └── settings.cpython-36.pyc
        │   └── settings.py
        ├── lib
        │   ├── convert.py
        │   ├── __init__.py
        │   ├── logger.py
        │   ├── response.py
        │   └── serializer.py
        ├── logs
        │   ├── error.log
        │   └── info.log
        ├── src
        │   ├── client.py
        │   ├── plugins
        │   │   ├── base.py
        │   │   ├── basic.py
        │   │   ├── cpu.py
        │   │   ├── disk.py
        │   │   ├── __init__.py
        │   │   ├── main_board.py
        │   │   ├── memory.py
        │   │   ├── nic.py
        │   └── run.py
        └── test
            ├── agent.py
            └── ssh.py