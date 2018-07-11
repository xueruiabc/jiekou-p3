from reInterface.testFengzhuang import TestApi
from common.get_excel import makedata
from common.log import LOG
from common.panduan import assertre

import ddt, unittest

data_test = makedata()


@ddt.ddt
class MyTest(unittest.TestCase):

    def setUp(self):
        LOG.info('测试用例开始执行')

    def tearDown(self):
        LOG.info('测试用例执行完毕')

    @ddt.data(*data_test)
    def test_api(self, data_test):
        api = TestApi(url=data_test['url'], token=data_test['token'], connent=data_test['coneent'],
                      fangshi=data_test['fangshi'])
        # LOG.info('输入参数：url:%s,token:%s,参数:%s,请求方式：%s'%(data_test['url'],data_test['token'],data_test['coneent'],
        #LOG.info('输入参数：url:%s,token:%s,参数:%s,请求方式：%s' % (data_test['url'], data_test['token'], data_test[ 'coneent'], data_test['fangshi']))
        LOG.info('输入参数：url:%s,token值:%s,参数:%s,请求方式：%s' % (
            data_test['url'], data_test['token'], data_test['coneent'], data_test['fangshi']))
        apijson = api.getJson()
        LOG.info('返回结果:%s' % apijson)
        qiwang1 = assertre(asserqingwang=data_test['qiwang'])
        self.assertEqual(int(dict(qiwang1)["code"]), dict(apijson)["code"], msg='预期和返回不一致')
