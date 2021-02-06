import allure
import pytest
import yaml

from pythontest.Calculator import Calculator

def get_datas(name,type='int'):

    with open('datas/calc.yml') as f:
        datas = yaml.safe_load(f)
        data = datas[name][type]['datas']
        ids = datas[name][type]['ids']
        return (data,ids)
#11
class TestCalc:

    add_int = get_datas('add','int')
    add_float = get_datas('add','float')
    div_int = get_datas('div','int')
    div_float = get_datas('div', 'float')
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

    @pytest.mark.parametrize('a,b,result',add_int[0],ids=add_int[1])
    def test_add(self,a,b,result):
        print('加法')
        assert result == self.cal.add(a, b)

    @pytest.mark.parametrize('a,b,result',add_float[0],ids=add_float[1])
    def test_add_float(self,a,b,result):
        print('浮点数加法')
        assert result == round(self.cal.add(a,b),2)


    @pytest.mark.parametrize('a,b,result',div_int[0],ids=div_int[1])
    def test_div(self,a,b,result):
        print('除法')
    #捕获异常
        with pytest.raises(ZeroDivisionError):
            assert result == self.cal.div(a, b)
    @pytest.mark.parametrize('a,b,result',div_float[0],ids=div_float[1])
    def test_div_flost(self,a,b,result):
        print('float除法')
        assert result == self.cal.div(a,b)