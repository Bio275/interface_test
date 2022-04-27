import requests

class Test_get:
    def test_get(self):
        host = "http://httpbin.org/"
        point = "get"
        url = "".join([host, point])
        params = {"show_env": "1", "test": "2"}
        headers = {"User-Agent": "test header"}
        r = requests.get(url, headers=headers, params=params)
        print(eval(r.text))