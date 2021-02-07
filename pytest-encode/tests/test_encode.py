import pytest

@pytest.mark.parametrize('name',['张毅','张飞'])
def test_encode(name):
    print(name)