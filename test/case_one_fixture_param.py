
import pytest

class TestCalc:

    def test_add(self,get_instance,get_fixture_datas_addint):
        print('加法')
        c = get_fixture_datas_addint
        assert c[2] == get_instance.add(c[0], c[1])


    def test_add_float(self,get_instance,get_fixture_datas_addfloat):
        print('浮点数加法')
        c=get_fixture_datas_addfloat
        assert c[2] == round(get_instance.add(c[0],c[1]),2)

    def test_div(self,get_instance,get_fixture_datas_divint):
        print('除法')
    #捕获异常
        c = get_fixture_datas_divint
        with pytest.raises(TypeError):
            assert c[2] == get_instance.div(c[1], c[2])

    def test_div_flost(self,get_instance,get_fixture_datas_divfloat):
        print('float除法')
        c =get_fixture_datas_divfloat
        assert c[2] == get_instance.div(c[0],c[1])