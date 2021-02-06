import yaml

def test_yaml():
    with open('./datas/calc.yml') as f:
        datas= yaml.safe_load(f)
        print(datas)
        # print(datas['add']['datas'])
        # print('--------------')
        # print(datas['div']['datas'])
        # print(datas['adiv']['datas2'])

        for i in datas:
           for j in datas[i]:
                a= datas[i][j]
    return  a

test_yaml()

