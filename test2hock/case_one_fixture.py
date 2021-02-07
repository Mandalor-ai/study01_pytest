import allure
import pytest
import yaml

from pythontest.Calculator import Calculator

def get_datas(name,type='int'):

    with open('datas/calc.yml',encoding='utf-8') as f:
        datas = yaml.safe_load(f)
        data = datas[name][type]['datas']
        ids = datas[name][type]['ids']
        return (data,ids)

@pytest.fixture()
def get_instance():
    print('开始计算')

    yield Calculator()
    print('结束计算')


class TestCalc:

    add_int = get_datas('add','int')
    add_float = get_datas('add','float')
    div_int = get_datas('div','int')
    div_float = get_datas('div', 'float')


    @pytest.mark.parametrize('a,b,result',add_int[0],ids=add_int[1])
    def test_add(self,get_instance,a,b,result):
        print('加法')
        assert result == get_instance.add(a, b)

    @pytest.mark.parametrize('a,b,result',add_float[0],ids=add_float[1])
    def test_add_float(self,get_instance,a,b,result):
        print('浮点数加法')
        assert result == round(get_instance.add(a,b),2)


    @pytest.mark.parametrize('a,b,result',div_int[0],ids=div_int[1])
    def test_div(self,get_instance,a,b,result):
        print('除法')
    #捕获异常
       # with pytest.raises(ZeroDivisionError):
        assert result == get_instance.div(a, b)


    @pytest.mark.parametrize('a,b,result',div_float[0],ids=div_float[1])
    def test_div_flost(self,get_instance,a,b,result):
        print('float除法')
        assert result == get_instance.div(a,b)