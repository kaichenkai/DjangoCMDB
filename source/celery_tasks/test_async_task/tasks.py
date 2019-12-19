# -*- coding: utf-8 -*-
import logging
from celery_tasks.main import app

logger = logging.getLogger("django")


@app.task(name="test_action")
def test_action(*args, **kwargs):
    """
    测试异步任务
    :param args:
    :param kwargs:
    :return:
    """

    print("完成异步任务!")
    logger.info("完成异步任务!")
