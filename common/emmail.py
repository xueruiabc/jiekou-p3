# -*- coding: utf-8 -*-
# @Author  : leizi
import smtplib, time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from common.log import LOG, logger


# 从配置文件中加载获取email的相关信息
def load_emil_setting():
    import yaml
    data_file = open(r".//config//email.yaml", "r")
    datas = yaml.load(data_file)
    data_file.close()
    return (datas['foremail'], datas['password'], datas['toeamil'], datas['title'])


def sendemail(filepath):  # 发送email
    from_addr, password, mail_to, mail_body = load_emil_setting()
    msg = MIMEMultipart()
    try:
        msg['Subject'] = '接口自动化测试报告'
        msg['From'] = '自动化测试平台'
        msg['To'] = mail_to
        msg['Date'] = time.strftime('%a, %d %b %Y %H:%M:%S %z')
        att = MIMEText(open(r'%s' % filepath, 'rb').read(), 'base64', 'utf-8')
        att["Content-Type"] = 'application/octet-stream'
        att["Content-Disposition"] ='attachment; filename='+(filepath.split("/")[-1])
        txt = MIMEText("这是测试报告的邮件，详情见附件", 'plain', 'gb2312')
        msg.attach(txt)
        msg.attach(att)
        # smtp = smtplib.SMTP()
        server = smtplib.SMTP_SSL("smtp.163.com", 465)
        server.login(from_addr, password)
        server.sendmail(from_addr, mail_to, msg.as_string())
        server.quit()
        LOG.info('邮件发送成功！')
    except Exception as e:
        LOG.info('邮件发送失败！原因是 %s' % e)


if __name__ == '__main__':
    sendemail("../result.txt")
