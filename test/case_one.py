import pytest
import yaml

from pythontest.Calculator import Calculator

def get_datas():

    with open('datas/calc.yml') as f:
        datas = yaml.safe_load(f)
        return (datas['add']['datas'],datas['add']['ids'],datas['div']['datas'],datas['div']['ids'])
#11
class TestCalc:

    datas:list = get_datas()

    def setup_class(self):
        print('实例化计算方法')
        self.cal = Calculator()

    def teardown_class(self):
        print('测试类执行完成')

    def setup(self):
        print('开始计算')
        self.cal = Calculator()

    def teardown(self):
        print('计算结束')

    @pytest.mark.parametrize('a,b,result',datas[0],ids=datas[1])
    def test_add(self,a,b,result):
        print('加法')
        assert result == self.cal.add(a, b)

    @pytest.mark.parametrize('a,b,result',datas[2],ids=datas[3])
    def test_div(self,a,b,result):
        print('除法')
        assert result == self.cal.div(a, b)
