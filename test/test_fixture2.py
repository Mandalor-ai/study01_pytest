from datetime import datetime

import pytest

#作用全局 每个方法前都先执行此方法
# @pytest.fixture(autouse=True)
#登出操作 相当于teardown  yield
@pytest.fixture()
def login():
    print('登录')
    token = datetime.now()
    yield token
    print('登出')

@pytest.fixture()
def get_username(login):
    print('zhang')


def test_serch():
    print('搜索')

@pytest.mark.usefixtures('get_username')
def test_cart():
    print('购物')

def test_order():
    print('下单')