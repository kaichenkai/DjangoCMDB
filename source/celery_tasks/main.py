# -*- coding: utf-8 -*-
from celery import Celery


import os
if not os.getenv("DJANGO_SETTINGS_MODULE"):
    os.environ["DJANGO_SETTINGS_MODULE"] = "cmdb.settings.dev"

app = Celery("test")
app.config_from_object("async_tasks.config")
app.autodiscover_tasks(["async_tasks.test_async_task", ])
