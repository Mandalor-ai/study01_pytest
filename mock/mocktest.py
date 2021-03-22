import json

from mitmproxy import ctx, http


class AD:
#MapLocal
    def request(self, flow):
        # 修改名字
        if "https://stock.xueqiu.com/v5/stock/batch/quote.json?_t=" in flow.request.pretty_url:
            with open("C:/Users/Admin/PycharmProjects/study01_pytest/mock/xuqiu.json", encoding="utf-8") as f:
                flow.response = http.HTTPResponse.make(200, f.read(), {"Content-Type": "text/html"})
                data = json.loads(flow.response.text)
                quote_list = data['data']['items']
                j = -0.01
                for i in range(len(quote_list)):
                    if i >= 1 and i < 4:
                        quote_list[i]['quote']['percent'] = str(j)
                        j += 0.01

                flow.response.text = json.dumps(data)
#rewirte
# def response(self, flow: http.HTTPFlow):
#     # 颜色边界值
#     if "https://stock.xueqiu.com/v5/stock/batch/quote.json?_t=" in flow.request.pretty_url:
#         # print(flow.response.text)
#         data = json.loads(flow.response.text)
#         quote_list = data['data']['items']
#         j = -0.01
#         for i in range(len(quote_list)):
#             if i >= 1 and i < 4:
#                 quote_list[i]['quote']['percent'] = str(j)
#                 j += 0.01
#
#         flow.response.text = json.dumps(data)


addons = [
    AD()
]
