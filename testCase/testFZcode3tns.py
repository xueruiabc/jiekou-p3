# -*- coding: utf-8 -*-
from reInterface.testFengzhuang import TestApi
from common.log import LOG
from common.get_excel import getdataByName

import ddt, unittest,json

re_url = 'http://192.168.12.25:8000/get.html'

@ddt.ddt
class MyTest(unittest.TestCase):

    def setUp(self):
        LOG.info('测试用例开始执行')

    def tearDown(self):
        LOG.info('测试用例执行完毕')

    #查询服务器信息
    data = getdataByName("FZTNScase", 1)
    @ddt.data(*data)
    def test_checkGo(self, data):
        # self.method = data['method']
        # par = eval(data['params'])
        # self.code = data['code']
        # self.msg = data['msg']
        # getApi = TestApi(url=re_url, connent=par, fangshi=self.method)
        # LOG.info('获取用户信息：%s,请求方式：%s' % (re_url, self.method))
        # getApiJso = getApi.getJson()
        # LOG.info('返回结果:%s' % getApiJso)
        # self.assertEqual(self.code, eval(getApiJso)["code"], msg='预期和返回不一致')
        self.lllcommon(data)

    #打开服务器
    data1 = getdataByName("FZTNScase", 2)
    @ddt.data(*data1)
    def test_turnOn(self, data1):
        # self.method = data1['method']
        # par = eval(data1['params'])
        # self.code = data1['code']
        # self.msg = data1['msg']
        # getApi = TestApi(url=re_url, connent=par, fangshi=self.method)
        # LOG.info('获取用户信息：%s,请求方式：%s' % (re_url, self.method))
        # getApiJso = getApi.getJson()
        # LOG.info('返回结果:%s' % getApiJso)
        # self.assertEqual(self.code, eval(getApiJso)["code"], msg='预期和返回不一致')
        self.lllcommon(data1)

    #关闭服务器
    data2 = getdataByName("FZTNScase", 3)
    @ddt.data(*data2)
    def test_turnOff(self, data2):
        # self.method = data2['method']
        # par = eval(data2['params'])
        # self.code = data2['code']
        # self.msg = data2['msg']
        # getApi = TestApi(url=re_url, connent=par, fangshi=self.method)
        # LOG.info('获取用户信息：%s,请求方式：%s' % (re_url, self.method))
        # getApiJso = getApi.getJson()
        # LOG.info('返回结果:%s' % getApiJso)
        # self.assertEqual(self.code, eval(getApiJso)["code"], msg='预期和返回不一致')
        self.lllcommon(data2)

    #配置
    data3 = getdataByName("FZTNScase", 4)
    @ddt.data(*data3)
    def test_ccc(self, data3):
        # self.method = data3['method']
        # par = eval(data3['params'])
        # self.code = data3['code']
        # self.msg = data3['msg']
        # getApi = TestApi(url=re_url, connent=par, fangshi=self.method)
        # LOG.info('获取用户信息：%s,请求方式：%s' % (re_url, self.method))
        # getApiJso = getApi.getJson()
        # LOG.info('返回结果:%s' % getApiJso)
        # self.assertEqual(self.code, eval(getApiJso)["code"], msg='预期和返回不一致')
        self.lllcommon(data3)

    def lllcommon(self,data0):
        self.method = data0['method']
        par = eval(data0['params'])
        self.code = data0['code']
        self.msg = data0['msg']
        getApi = TestApi(url=re_url, data_parms=par, fangshi=self.method)
        LOG.info('获取用户信息：%s,请求方式：%s' % (re_url, self.method))
        getApiJso = getApi.getJson()
        LOG.info('返回结果:%s' % getApiJso)
        self.assertEqual(self.code, eval(getApiJso)["code"], msg='预期和返回不一致')
