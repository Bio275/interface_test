import json

import ddt


class SendRequests:
    # 接口请求方法（s通过传递request的session）
    def sendrequests(self, s, apidata):
        try:
            url = apidata["url"]
            method = apidata["method"]
            if apidata["params"] == "":
                par = None
            else:
                par = eval(apidata["params"])
            if apidata["headers"] == "":
                h = None
            else:
                h = eval(apidata["headers"])
            if apidata["body"] == "":
                body_data = None
            else:
                body_data = eval(apidata["body"])
            type = apidata["type"]
            if type == "data":
                body = body_data
            # 请求体是json格式的话，需要转换一下
            if type == "json":
                body = json.dumps(body_data)
            else:
                body = body_data

            re = s.request(method=method, url=url, headers=h, params=par, data=body, verify=False)
            return re
        except Exception as e:
            print(e)
