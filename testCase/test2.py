import hashlib
import ast

from reInterface.testFengzhuang import TestApi
from common.get_excel import getdata
from common.log import LOG
from common.panduan import assertre

import ddt, unittest

data_test = getdata()
# TODO: 请根据需要，换成您的HOST，app_key和app_secrect
API_URL = 'http://hn2.api.okayapi.com/'
APP_KEY = 'F92F0D33882131C09423F4C789328FAA'
APP_SECRET = 'gRyfd8WIwbtvD2u9TTKMP81E5wdAw9H7aWnNx3Mm0aTeKIOl4IG8nPxMGiUll08rWCmdOTSCALk'
APP_S = 'App.User.Login'

# 生成签名
def Signature(params, key=None, secret=None):
    key = key or APP_KEY
    secret = secret or APP_SECRET
    # params.pop('app_secrect', None)
    params['app_key'] = key
    md5_ctx = hashlib.md5()
    str1 = ''.join([params[value] for value in sorted([key for key in params])])
    print(str1)
    md5_ctx.update((str1 + secret).encode("utf-8"))
    return md5_ctx.hexdigest().upper()

@ddt.ddt
class MyTest(unittest.TestCase):

    def setUp(self):
        LOG.info('测试用例开始执行')

    def tearDown(self):
        LOG.info('测试用例执行完毕')

    @ddt.data(*data_test)
    def test_bapi(self, data_test):
        # params = ast.literal_eval(data_test['coneent'])
        params ={}
        params['s']=APP_S
        params['username'] = data_test['username']
        params['password'] = data_test['password']
        params['sign'] = Signature(params)
        api = TestApi(url=API_URL, connent=params,fangshi=data_test['fangshi'])
        LOG.info('输入参数：url:%s,参数:%s,请求方式：%s' % (
            API_URL,  params, data_test['fangshi']))
        apijson = api.getJson()
        LOG.info('返回结果:%s' % apijson)
        # qiwang1 = assertre(asserqingwang=data_test['qiwang'])
        # self.assertEqual(int(dict(qiwang1)["code"]), dict(apijson)["code"], msg='预期和返回不一致')
        self.assertEqual(int(data_test['qiwang']), dict(apijson)["code"], msg='预期和返回不一致')