import yaml
def test_yaml():
    with open('./datas/calc.yml') as f:
        datas= yaml.safe_load(f)
        print(datas)
        print(datas['add']['datas'])
        print('--------------')
        print(datas['div']['datas'])
        # print(datas['adiv']['datas2'])