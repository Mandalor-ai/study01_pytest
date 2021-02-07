#案例执行顺序
import pytest


@pytest.mark.run(order=1)
def test_1():
    print('1')
@pytest.mark.run(order=3)
def test_2():
    print('1')
@pytest.mark.run(order=3)
def test_3():
    print('1')
@pytest.mark.run(order=2)
def test_4():
    print('1')