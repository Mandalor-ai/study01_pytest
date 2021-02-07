#hocksper.py 文件中收集测试用例的方法
#打包需要两个依赖   setuptools  wheel
#命令行执行python setup.py sdist bdist_wheel  打包命令
#打包成功后  在文件夹下新建两个文件 build  dist
#再命令行执行 pip install C:\Users\Admin\PycharmProjects\study01_pytest\pytest-encode\dist\pytest_encode-1.0-py3-none-any.whl 进行安装
from typing import List

import pytest
from _pytest.config import Config
from requests import Session


def pytest_collection_modifyitems(
        session: "Session", config: "Config", items: List["Item"]
) -> None:
    print('------------')
    print(items)
    # for item in items:
    #     item.name = item.name.encode('utf-8').decode('unicode-escape')
    #     item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')
        print('------执行名称----------')
        print(item.name)
        print('-------执行路径---------')
        print(item._nodeid)
