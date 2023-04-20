import pytest

from linkevent.all_request import Request_Way


def setup_module(module):
    print("所有用例执行前执行一次")


def teardown_module(module):
    print("所有用例执行完执行一次")


def setup_function(function):
    print("每个用例执行前执行一次")


def teardown_function(function):
    print("每个用例执行完执行一次")


def test01():
    url = "http://test.allapp.link/LVHNuLuP2neGQXJ5Bt5TAV"

    res = Request_Way().get(url=url)

    result = 200
    assert res.status_code == result


def test02():
    assert 1



