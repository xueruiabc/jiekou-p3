# -*- coding: utf-8 -*-
# @Time    : 2017/6/4 20:35
# @Author  : lileilei
# @File    : get_excel.py
# @Software: PyCharm
import xlrd
import json
from common.log import LOG,logger
import hashlib

@logger('解析测试用例文件')
def datacel():
    # filepath = '..\\test_case\\case.xlsx'#路径问题
    # file = xlrd.open_workbook(filepath)
    try:
        filepath = '.\\test_case\\case.xlsx'
        file = xlrd.open_workbook(filepath)
        me = file.sheets()[2]
        nrows = me.nrows
        listid = []
        listToken = []
        listconeent = []
        listurl = []
        listfangshi = []
        listqiwang = []
        # listrelut=[]
        listname = []
        for i in range(1, nrows):
            listid.append(me.cell(i, 0).value)
            listToken.append(me.cell(i, 2).value)
            # xx = me.cell(i, 3).value
            # print(xx)
            # if xx != '':
            #     listconeent.append(eval(xx))
            # else:
            #     listconeent.append(None)
            # listconeent.append(json.load(me.cell(i,3).value))
            listconeent.append(me.cell(i, 3).value)
            listurl.append(me.cell(i, 4).value)
            listname.append(me.cell(i, 1).value)
            listfangshi.append((me.cell(i, 5).value))
            listqiwang.append((me.cell(i, 6).value))
        return listid, listToken, listconeent, listurl, listfangshi, listqiwang, listname
    except:
        LOG.info('打开测试用例失败，原因是:%s' % Exception)
        print(Exception)


@logger('生成数据驱动所用数据')
def makedata():
    listid, listToken, listconeent, listurl, listfangshi, listqiwang, listname = datacel()
    make_data = []
    for i in range(len(listid)):
        make_data.append({'url': listurl[i], 'token': listToken[i], 'coneent': listconeent[i], 'fangshi': listfangshi[i],
                          'qiwang': listqiwang[i]})
        i += 1
    return make_data

@logger('获取测试用例数据')
def getxls(xlsname):

    try:
        filepath = '.\\test_case\\'+xlsname+".xlsx"
        file = xlrd.open_workbook(filepath)
        me = file.sheets()[0]
        # me = file.sheet_by_name('login')
        nrows = me.nrows
        listname = []
        listfangshi = []
        listUsername = []
        listpassword = []
        listqiwang = []
        listmsg=[]
        for i in range(1, nrows):
            listname.append(me.cell(i, 0).value)
            listfangshi.append(me.cell(i,1).value)
            listUsername.append(me.cell(i, 2).value)
            pw = str(me.cell(i, 3).value)
            listpassword.append(hashlib.md5(pw.encode("utf-8")).hexdigest())#md5加密
            listqiwang.append(me.cell(i, 4).value)
            listmsg.append(me.cell(i,5).value)
        return listname,listfangshi,listUsername,listpassword,listqiwang,listmsg
    except:
        LOG.info('打开测试用例失败，原因是:%s' % Exception)
        print(Exception)

@logger('----生成数据驱动所用数据!!')
def getdata(xlsname):
    listname, listfangshi, listUsername, listpassword, listqiwang, listmsg = getxls(xlsname)
    get_data = []
    for i in range(len(listname)):
        get_data.append(
            {'username': listUsername[i], 'password': listpassword[i], 'fangshi': listfangshi[i],
             'qiwang': listqiwang[i],'msg':listmsg[i]})
        i += 1
    return get_data

@logger("获取数据信息")
def getdataByName(xlsname,sheet):
    try:
        filepath =  '.\\test_case\\'+xlsname+".xlsx"
        file = xlrd.open_workbook(filepath)
        me = file.sheets()[sheet-1]
        nrows = me.nrows
        # listname = []
        # listmethod = []
        # listparams = []
        # listcode = []
        # listmsg = []
        get_data = []
        for i in range(1,nrows):
            get_data.append(
                {"casename":me.cell(i,0).value,
                 "method":me.cell(i,1).value,
                 "params":me.cell(i,2).value,
                 "code":int(me.cell(i,3).value),
                 "msg":me.cell(i,4).value
                 }
            )
            i +=1
            # listname.append(me.cell(i,0).value)
            # listmethod.append(me.cell(i,1).value)
            # listparams.append(me.cell(i,2).value)
            # listcode.append(me.cell(i,3).value)
            # listmsg.append(me.cell(i,4).value)
        return get_data
    except:
        LOG.info('打开测试用例失败，原因是:%s' % Exception)
        print(Exception)


if __name__=="__main__":
    d = getdataByName("FZcase")
    print(d)