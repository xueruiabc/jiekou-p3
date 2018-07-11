# -*- coding: utf-8 -*-
# @Author  : leizi
# from testCase.test2 import MyTest
import unittest, time, os
from common.log import LOG
from common import BSTestRunner


class RunAllCases:

    def __init__(self):
        """
            初始化，
            resultPath：测试报告的路径和文件名
            caseFile：测试用例的路径
            caseList：用于存放测试用例名称

        """
        global resultPath
        now = time.strftime('%Y-%m%d%H%M', time.localtime(time.time()))
        basedir = os.path.abspath(os.path.dirname(__file__))
        file_dir = os.path.join(basedir, 'test_Report')
        resultPath = os.path.join(file_dir, (now + '.html'))
        self.caseFile = os.path.join(basedir, 'testCase')
        self.caseList = []

    def setCasesSuite(self):
        """
        设置 测试用例集
        :return:
        """
        # test_suite = unittest.TestSuite()
        # discover = unittest.defaultTestLoader.discover(self.caseFile, pattern='test2.py', top_level_dir=None)
        # test_suite.addTest(discover)
        discover = unittest.defaultTestLoader.discover(self.caseFile, pattern='testFZcode*.py', top_level_dir=None)
        return discover
        #批量添加
        # for testsuite in discover:
        #     for test_case in testsuite:
        #         test_suite.addTest(test_case)
        # return test_suite


    def run(self):
        try:
            LOG.info("********************Test   Start********************")
            suit = self.setCasesSuite()
            if suit is not None:
                re_open = open(resultPath, 'wb')
                runner = BSTestRunner.BSTestRunner(stream=re_open, title='接口测试报告', description='测试结果')
                m = runner.run(suit)
                re_open.close()
            else:
                LOG.info("********************没有用例执行********************")
        except Exception as ex:
            LOG.error(str(ex))
        finally:
            LOG.info("********************Test  End********************")


if __name__ == '__main__':
    obz = RunAllCases()
    obz.run()
