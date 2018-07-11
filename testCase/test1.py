import ddt , unittest
import requests

# def t():
#     url = 'http://httpbin.org/cookies'
#     cookies = dict(cookies_are='working',lalal='test')
#     r = requests.get(url, cookies=cookies)
#     print(r.content)
#     print(r.cookies)
#     print(r.url)

@ddt.ddt
class Demotest(unittest.TestCase):

    def setUp(self):
        print('测试用例开始执行')
        print("+++++")

    def tearDown(self):
        print('测试用例执行完毕')
        print("******")

    @ddt.data(2,3)
    def test_api(self, data_test):
        print(data_test)

    @ddt.data([2, 3], [3, 5])
    @ddt.unpack
    def testv(self, fir, xx):
        print(fir+xx)

    @ddt.data([2, 3], [3, 5])
    def testm(self, fir):
        print(fir)

    @ddt.file_data('../config/email.yaml')
    def testA(self, fir):
        print(fir)

    @ddt.data(1, 2, 3)
    # 定义一个value用于接收我们传入的参数
    def test_something(self, value):
        # 对于传入的参数与2进行对比,相等就通过,否则就是不同过
        self.assertEqual(value, 2)


if __name__=="__main__":
    # unittest.main()
    t()