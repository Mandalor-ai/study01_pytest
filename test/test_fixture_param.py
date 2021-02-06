#参数化fixture
import pytest


@pytest.fixture(params=['zhang','shuang','qian'])
def login(request):
    print('login')
    return request.param

def test_serch(login):
    print(login)
    print('serch')