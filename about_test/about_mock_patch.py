from unittest import mock

import pytest
import requests

class WhereIsPythonError(Exception):
    pass


def is_python_still_a_programming_language():
    try:
        # http://python.orgにGETリクエストしてレスポンスを取得
        r = requests.get('http://python.org')
    except IOError:
        pass
    else:
        # 例外が発生しない、かつ、レスポンスのステータスコードが200の場合、
        # レスポンスボディのテキストに指定の文字列が含まれるか否かの結果を真偽値で返す
        if r.status_code == 200:
            # print(r.text)
            return 'Python is a programming language' in r.text
    raise WhereIsPythonError('Something bad happened')

def get_fake_get(status_code, text):
    m = mock.Mock()
    m.status_code = status_code
    m.text = text

    def fake_get(url):
        return m

    return fake_get

def raise_get(url):
    raise IOError('Unable to fetch url %s' % url)

# get_fake_get()の第2引数として渡した文字列をr.textに代入している
# @mock.patch('requests.get', get_fake_get(200, 'Python is a programming language'))
# def test_python_is():
#     assert is_python_still_a_programming_language() is True
# test_python_is()

# get_fake_get()の第2引数として渡した文字列をr.textに代入している
# @mock.patch('requests.get', get_fake_get(200, 'Python is no more a programming language'))
# def test_python_is_not():
#     assert is_python_still_a_programming_language() is False
# test_python_is_not()

# 例外WhereIsPythonErrorが送出されていなければDID NOT RAISESを出力する
# 正しい例外が送出されているかのテストで利用できる（with pytest.raises()）
# @mock.patch('requests.get', get_fake_get(404, 'Whatever'))
# def test_bad_status_code():
#     with pytest.raises(WhereIsPythonError):
#         is_python_still_a_programming_language()
#         # 1 /1
# test_bad_status_code()

# IOErrorを強制的に創出させている
# @mock.patch('requests.get', raise_get('http://python.org'))
# def test_ioerror():
#     with pytest.raises(WhereIsPythonError):
#         is_python_still_a_programming_language()