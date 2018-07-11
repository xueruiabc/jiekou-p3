# -*- coding: utf-8 -*-
from reInterface.testFengzhuang import TestApi
from common.log import LOG
from common.get_excel import getdataByName

import ddt, unittest,json

preCodeUrl = 'http://192.168.12.162:8080/CodeSystem/'

@ddt.ddt
class MyTest(unittest.TestCase):

    def setUp(self):

        LOG.info('测试用例开始执行')


    def tearDown(self):
        LOG.info('测试用例执行完毕')

    #配置某一编码可分配的前段码分配范围
    data = getdataByName("FZcase", 5)
    @ddt.data(*data)
    def test_updatePreCodeScope(self, data):
        self.method = data['method']
        par = eval(data['params'])
        self.code = data['code']
        self.msg = data['msg']
        re_url = preCodeUrl + "organization/findList"
        getApi = TestApi(url=re_url, data_parms=par, fangshi=self.method)
        LOG.info('获取用户信息：%s,请求方式：%s' % (re_url, self.method))
        getApiJso = getApi.getJson()
        LOG.info('返回结果:%s' % getApiJso)
        self.assertEqual(self.code, eval(getApiJso)["code"], msg='预期和返回不一致')

    # 添加编码类型
    data6 = getdataByName("FZcase", 6)
    @ddt.data(*data6)
    def test_codeTypeInsert(self, data6):
        re_url = preCodeUrl + "codeType/insert"
        self.method = data6['method']
        par = eval(data6['params'])
        self.code = data6['code']
        self.msg = data6['msg']
        getApi = TestApi(url=re_url, json_parms=par, fangshi=self.method)
        LOG.info('获取用户信息：%s,请求方式：%s' % (re_url, self.method))
        getApiJso = getApi.getJson()
        LOG.info('返回结果:%s' % getApiJso)
        self.assertEqual(self.code, eval(getApiJso)["code"], msg='预期和返回不一致')

    # 查询编码类型，可根据多条件查询，也可根据但条件查询
    data7 = getdataByName("FZcase", 7)
    @ddt.data(*data7)
    def test_codeTypeQueryByCondition(self, data7):
        re_url = preCodeUrl + "codeType/queryByCondition"
        self.method = data7['method']
        par = eval(data7['params'])
        self.code = data7['code']
        self.msg = data7['msg']
        getApi = TestApi(url=re_url, data_parms=par, fangshi=self.method)
        LOG.info('获取用户信息：%s,请求方式：%s' % (re_url, self.method))
        getApiJso = getApi.getJson()
        LOG.info('返回结果:%s' % getApiJso)
        self.assertEqual(self.code, eval(getApiJso)["code"], msg='预期和返回不一致')