# -*- coding: utf-8 -*-
# @Time    : 2017/6/4 20:36
# @Author  : lileilei
# @Site    : 
# @File    : testFengzhuang.py
from reInterface.test_requests import requ
from common.log import LOG,logger
import json

reques = requ()


class TestApi(object):
    def __init__(self, url,fangshi, data_parms=None,json_parms=None):
        self.url = url
        self.data_p = data_parms
        self.json_p = json_parms
        self.fangshi = fangshi

    def testapi(self):
        if self.fangshi == 'POST':
            response = reques.post(self.url, d_parms=self.data_p,j_parms=self.json_p)
        elif self.fangshi == "GET":
            response = reques.get(url=self.url, parms=self.data_p)
        else:
            LOG.info('请求方式不是POST或GET')
        return response

    def getText(self):
        data_text = self.testapi()
        return data_text

    def getJson(self):
        json_data = json.dumps(self.testapi(),ensure_ascii=False)
        return json_data

