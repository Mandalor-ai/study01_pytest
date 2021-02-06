import pytest


@pytest.fixture()
def login():
    print('登录')

@pytest.fixture()
def get_username():
    print('zhang')


def test_serch(login,get_username):
    print('搜索')

@pytest.mark.usefixtures('login')
def test_cart():
    print('购物')

@pytest.mark.usefixtures('get_username')
@pytest.mark.usefixtures('login')
def test_order():
    print('下单')