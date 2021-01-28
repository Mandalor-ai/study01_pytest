#基础案例练习
from pythoncode.Calculator import Calculator

calu= Calculator()

def test_div():#除法
    assert 2==calu.div(3,0)
def test_add():#加法
    assert 3==calu.add(1,2)
def test_sub():#减法
    assert 6==calu.subtraction(9,7)
def test_ride():#乘法
    assert 63==calu.ride(9,7)
def test_a():
    assert  1!=2