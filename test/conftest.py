#conftest.py  文件名固定格式 不能改动
import datetime

import pytest

#通过conftest.py  定义session级别
#@pytest.fixture(scope='session')
# def login():
#     print('登录')
#     token =datetime.datetime.now()
#     yield token
#     print('登出')
import yaml

from pythontest.Calculator import Calculator

def get_datas(name,type='int'):

    with open('datas/calc.yml') as f:
        datas = yaml.safe_load(f)
        data = datas[name][type]['datas']
        ids = datas[name][type]['ids']
        return (data,ids)

@pytest.fixture(scope='function')
def get_instance():
    print('开始计算')
    yield Calculator()
    print('结束计算')

@pytest.fixture(params=get_datas('add','int')[0],ids=get_datas('add','int')[1],scope='session')
def get_fixture_datas_addint(request):
    res = request.param
    return res

@pytest.fixture(params=get_datas('add','float')[0],ids=get_datas('add','float')[1],scope='session')
def get_fixture_datas_addfloat(request):
    res = request.param
    return res

@pytest.fixture(params=get_datas('div','int')[0],ids=get_datas('div','int')[1],scope='session')
def get_fixture_datas_divint(request):
    res = request.param
    return res
@pytest.fixture(params=get_datas('div','float')[0],ids=get_datas('div','float')[1],scope='session')
def get_fixture_datas_divfloat(request):
    res = request.param
    return res