import allure
import requests


class Request_Way():

    @allure.step("发送get请求")
    def get(self, url, params=None, **kwargs):
        return requests.get(url=url, params=params, **kwargs)

    @allure.step("发送post请求")
    def post(self, url, data=None, json=None, **kwargs):
        return requests.get(url=url, data=data, json=json, **kwargs)

    @allure.step("发送put请求")
    def put(self, url, data=None, headers=None, **kwargs):
        return requests.get(url=url, headers=headers, data=data, **kwargs)


if __name__ == '__main__':
    re = Request_Way()

    res = re.get(url="http://test.allapp.link/LVHNuLuP2neGQXJ5Bt5TAV")

    print(res.status_code)
