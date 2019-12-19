# -*- coding: utf-8 -*-
import os
import sys
# 插入 asset_collection 导包路径
BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASEDIR)
from src.run import run


if __name__ == '__main__':
    run()
