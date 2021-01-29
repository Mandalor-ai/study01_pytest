#基础案例练习
from pythoncode.Calculator import Calculator





class TestCalc:

    #初始化
    def setup(self):
        self.calu = Calculator() # 实例化计算方法
    def test_add(self):  # 加法
        assert 3 == calu.add(1, 2)

    def test_div(self):  # 除法
        assert 2 == calu.div(3, 0)