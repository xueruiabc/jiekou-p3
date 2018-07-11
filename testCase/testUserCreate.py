import hashlib
import ast

from reInterface.testFengzhuang import TestApi
from common.get_excel import getdata
from common.log import LOG
from common.panduan import assertre

import requests

import ddt, unittest


# TODO: 请根据需要，换成您的HOST，app_key和app_secrect
API_URL = 'https://hn2.api.okayapi.com/'
APP_KEY = 'F92F0D33882131C09423F4C789328FAA'
APP_SECRET = 'gRyfd8WIwbtvD2u9TTKMP81E5wdAw9H7aWnNx3Mm0aTeKIOl4IG8nPxMGiUll08rWCmdOTSCALk'
APP_S = 'App.User.Login'

# 生成签名
def Signature(params, key=None, secret=None):
    # key = key or APP_KEY
    secret = secret or APP_SECRET
    # params.pop('app_secrect', None)
    # params['app_key'] = key
    md5_ctx = hashlib.md5()
    str1 = ''.join([params[value] for value in sorted([key for key in params])])
    print(str1)
    md5_ctx.update((str1 + secret).encode("utf-8"))
    return md5_ctx.hexdigest().upper()

# data_test = getdata()

@ddt.ddt
class MyTest(unittest.TestCase):

    def setUp(self):
        LOG.info('测试用例开始执行')
        self.token1 = "A7374BC90007F55E6DA0D7DACE17D4F8D2E2B6B45B00100D96332D5F3FB1D803"
        self.uuid = '7CADFA0ACED6FD8D767471CAB1304E3E'
        LOG.info("用户uuid：%s" % self.uuid)
        LOG.info("用户token：%s" % self.token1)
        # self.assertEqual(int(data_test['qiwang']), dict(apijson)["code"], msg='预期和返回不一致')

    def tearDown(self):
        LOG.info('测试用例执行完毕')

    # @ddt.data(2)
    # def test_bapi(self,s):
    #     print(s)
    #     par ={}
    #     par['s']= 'App.User_Meta.Create'
    #     par['uuid']=self.uuid
    #     par['token']=self.token1
    #     par['app_key']=APP_KEY
    #     par['key'] = "favorite"
    #     par['data'] = "{\"kk\":\"football\",\"ll\":\"swim\",\"qq\":\"reading,jump\"}"
    #     par['visiable'] = 'protected'
    #     par['sign']=Signature(par)
    #     print(par['sign'])
    #     getApi = TestApi(url=API_URL,token=self.token1,connent=par,fangshi='POST')
    #     LOG.info('获取用户信息：%s,请求方式：%s' % ('ccc','POST'))
    #     getApiJso = getApi.getJson()
    #     LOG.info('返回结果:%s' % getApiJso)

    @ddt.data(2)
    def test_gapi(self,s):
        print(s)
        gpar ={}
        gpar['s']= 'App.User_Meta.Get'
        gpar['uuid']=self.uuid
        gpar['token']=self.token1
        gpar['app_key']=APP_KEY
        gpar['key'] = "favorite"
        gpar['fields'] = "kk"
        gpar['sign']=Signature(gpar)
        print(gpar['sign'])
        getApi = TestApi(url=API_URL,connent=gpar,fangshi='POST')
        # getApiJso = requests.post(API_URL,data=gpar)
        LOG.info('获取用户信息：%s,请求方式：%s' % ('ccc','POST'))
        getApiJso = getApi.getJson()
        print(getApiJso)
        LOG.info('返回结果:%s' % getApiJso)