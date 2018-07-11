# -*- coding: utf-8 -*-
from reInterface.testFengzhuang import TestApi
from common.log import LOG
from common.get_excel import getdataByName

import ddt, unittest,json

baseUrl = 'http://192.168.12.162:8080/CodeSystem/'

@ddt.ddt
class MyTest(unittest.TestCase):

    def setUp(self):

        LOG.info('测试用例开始执行')


    def tearDown(self):
        LOG.info('测试用例执行完毕')


    #添加后段码
    data1 = getdataByName("FZSucase", 1)
    @ddt.data(*data1)
    def test_batchInsert(self, data1):
        self.url = data1['casename']
        self.method = data1['method']
        par = eval(data1['params'])
        self.code = data1['code']
        self.msg = data1['msg']
        re_url = baseUrl + self.url
        getApi = TestApi(url=re_url, json_parms=par, fangshi=self.method)
        LOG.info('获取用户信息：%s,请求方式：%s' % (re_url, self.method))
        getApiJso = getApi.getJson()
        LOG.info('返回结果:%s' % getApiJso)
        self.assertEqual(self.code, eval(getApiJso)["code"], msg='预期和返回不一致')
        self.assertEqual(self.msg, eval(getApiJso)["result"], msg='预期和返回不一致')


    #查询后段码，可根据多条件查询，也可根据单条件查询
    data2 = getdataByName("FZSucase", 2)
    @ddt.data(*data2)
    def test_findSuffixList(self, data2):
        self.url = data2['casename']
        self.method = data2['method']
        par = eval(data2['params'])
        self.code = data2['code']
        self.msg = data2['msg']
        re_url = baseUrl + self.url
        getApi = TestApi(url=re_url, data_parms=par, fangshi=self.method)
        LOG.info('获取用户信息：%s,请求方式：%s' % (re_url, self.method))
        getApiJso = getApi.getJson()
        LOG.info('返回结果:%s' % getApiJso)
        self.assertEqual(self.code, eval(getApiJso)["code"], msg='预期和返回不一致')

    #修改后段码
    data3 = getdataByName("FZSucase", 3)
    @ddt.data(*data3)
    def test_modifySuffixCode(self, data3):
        self.url = data3['casename']
        self.method = data3['method']
        par = eval(data3['params'])
        self.code = data3['code']
        self.msg = data3['msg']
        # re_url = baseUrl + self.url
        re_url = "http://192.168.12.25:8080/CodeSystem/"+self.url
        getApi = TestApi(url=re_url, json_parms=par, fangshi=self.method)
        LOG.info('获取用户信息：%s,请求方式：%s' % (re_url, self.method))
        getApiJso = getApi.getJson()
        LOG.info('返回结果:%s' % getApiJso)
        self.assertEqual(self.code, eval(getApiJso)["code"], msg='预期和返回不一致')
        self.assertEqual(self.msg, eval(getApiJso)["result"], msg='预期和返回不一致')
