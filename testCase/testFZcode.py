# -*- coding: utf-8 -*-
from reInterface.testFengzhuang import TestApi
from common.log import LOG
from common.get_excel import getdataByName
# from common.panduan import assertre

import ddt, unittest,json

preCodeUrl = 'http://192.168.12.162:8080/CodeSystem/preCode/'

@ddt.ddt
class MyTest(unittest.TestCase):

    def setUp(self):

        LOG.info('测试用例开始执行')


    def tearDown(self):
        LOG.info('测试用例执行完毕')

    #前段码分配,
    #目前没有使用
    data1 = getdataByName("FZcase", 1)
    @ddt.data(*data1)
    # @unittest.skip('暂时跳过用例的测试,目前没有使用')
    def test_insert(self, data1):
        self.method = data1['method']
        par = eval(data1['params'])
        self.code = data1['code']
        self.msg = data1['msg']
        re_url = preCodeUrl + "insert"
        getApi = TestApi(url=re_url, json_parms=par, fangshi=self.method)
        LOG.info('获取用户信息：%s,请求方式：%s' % (re_url, self.method))
        getApiJso = getApi.getJson()
        LOG.info('返回结果:%s' % getApiJso)

    #分页多条件查询前段码
    data2 = getdataByName("FZcase",2)
    @ddt.data(*data2)
    def test_findListPage(self,data2):
        reUrl = preCodeUrl+"findListPage"
        self.method = data2['method']
        par = eval(data2['params'])
        self.code = data2['code']
        self.msg = data2['msg']
        print(data2)
        getApi = TestApi(url=reUrl,data_parms=par,fangshi=self.method)
        LOG.info('获取用户信息：%s,请求方式：%s' % (reUrl,self.method))
        getApiJso = getApi.getJson()
        LOG.info('返回结果:%s' % getApiJso)

    #查询编码类型所对应的可分配前段码范围
    data3 = getdataByName("FZcase",3)
    @ddt.data(*data3)
    def test_queryPreCodeScope(self,data3):
        re_url = preCodeUrl + "queryPreCodeScope"
        self.method = data3['method']
        # par = eval(data3['params'])
        par = {"codeName":"ecode111"}
        self.code = data3['code']
        self.msg = data3['msg']
        getApi = TestApi(url=re_url, data_parms=par, fangshi=self.method)
        LOG.info('获取用户信息：%s,请求方式：%s' % (re_url, self.method))
        getApiJso = getApi.getJson()
        LOG.info('返回结果:%s' % getApiJso)

    #配置某一编码可分配的前段码分配范围
    #伪接口
    data4 = getdataByName("FZcase", 4)
    @ddt.data(*data4)
    def test_updatePreCodeScope(self, data4):
        self.method = data4['method']
        par = eval(data4['params'])
        self.code = data4['code']
        self.msg = data4['msg']
        re_url = preCodeUrl + "updatePreCodeScope"
        getApi = TestApi(url=re_url, data_parms=par, fangshi=self.method)
        LOG.info('获取用户信息：%s,请求方式：%s' % (re_url, self.method))
        getApiJso = getApi.getText()
        LOG.info('返回结果:%s' % getApiJso)

