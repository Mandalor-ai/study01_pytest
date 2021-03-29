import json

import pytest
import requests
from requests import request


class TestDemo:
    def setup(self):
        self.token = self.test_get_token()

    # 获取token
    def test_get_token(self):
        corpid = 'ww1c882640ab082132'
        corpsecret = 'AR9oLkVl7oDCVyoVwXXV9lyGTQ4_KQu8aF0nleQ_5QA'
        r = requests.get(f'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}')
        token = r.json()['access_token']
        return token

    # 创建成员

    def test_creat_mans(self):
        datas = {
            "userid": "zs9999",
            "name": "张三丰",
            "mobile": "13800000999",
            "department": [1]}
        url = f'https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={self.token}'
        r = requests.post(url, json.dumps(datas))
        print(r.json())

    # 读取成员
    def test_read_man(self):
        userid = 'zs9999'
        r = requests.get(f'https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={self.token}&userid={userid}')
        print(r.json())

    # 更新成员
    def test_update_man(self):
        data = {
            "userid": "zs9999",
            "name": "张四丰",
            "mobile": "13800000066",
            "department": [1]}
        url = f'https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={self.token}'
        r = requests.post(url,json.dumps(data))
        print(r.json())

    # 删除成员
    def test_delete_man(self):
        userid = 'zs9999'
        r = requests.get(f'https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={self.token}&userid={userid}')
        print(r.json())
