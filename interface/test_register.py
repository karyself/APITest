# -*- coding: utf-8 -*-
# IVS7.0：3.3 用户注册
import requests
import unittest
from HTMLTestRunner import HTMLTestRunner
import sys
if sys.getdefaultencoding()!='utf-8':
    reload(sys)
    sys.setdefaultencoding('utf-8')

class Register(unittest.TestCase):
    """ 测试用户注册接口，测试路径使用单条用例实现 """

    def setUp(self):
        self.url = 'http://172.16.36.233:7757/service/user/register'

    #@unittest.skip('IVS7.0存在缺陷：参数为空都能新增用户成功，包括必填项')
    @unittest.skip('skip 1')
    def test_register_all_null(self):
        """ 所有参数为空 """
        d = {'type': '', 'id': '', 'passwd': '', 'nickname': '', 'photo': '', 'sex': '', 'sp': '', 'vcode': ''}
        r = requests.post(self.url, data=d)
        self.result = r.text
        self.assertEqual(r.status_code, 200)
        print r.text

    #@unittest.skip('IVS7.0存在缺陷：参数为空都能新增用户成功，包括必填项')
    @unittest.skip('skip 2')
    def test_register_must_exist_null(self):
        """ 必填项存在空 """
        d = {'type': '0', 'id': '', 'passwd': '', 'nickname': '', 'photo': '', 'sex': '', 'sp': '', 'vcode': ''}
        r = requests.post(self.url, data=d)
        self.assertEqual(r.status_code, 200)
        print r.text

    def test_register_id_format_error(self):
        """ 手机号格式输入不正确（type=1）"""
        d = {'type': '1', 'id': '1370000', 'passwd': '1testing', 'nickname': '', 'photo': '', 'sex': '', 'sp': '', 'vcode': ''}
        r = requests.post(self.url, data=d)
        self.assertEqual(r.status_code, 200)
        print r.text

    def test_register_id_is_exist(self):
        """ id已经存在 """
        d = {'type': '0', 'id': 'teacher', 'passwd': '1testing', 'nickname': '', 'photo': '', 'sex': '', 'sp': '', 'vcode': ''}
        r = requests.post(self.url, data=d)
        self.assertEqual(r.status_code, 200)
        print r.text

    def test_register_sp_is_not_exist(self):
        """ 渠道id不存在"""
        d = {'type': '0', 'id': 'test04', 'passwd': '1testing', 'nickname': 'test04', 'photo': '', 'sex': '', 'sp': '1001', 'vcode': ''}
        r = requests.post(self.url, data=d)
        self.assertEqual(r.status_code, 200)
        print r.text

    def test_register_success(self):
        """ 注册成功 """
        d = {'type': '0', 'id': 'test05', 'passwd': '1testing', 'nickname': 'test05', 'photo': '', 'sex': '', 'sp': 'huawei', 'vcode': ''}
        r = requests.post(self.url, data=d)
        self.assertEqual(r.status_code, 200)
        print r.text

    def tearDown(self):
        pass


'''
# 去掉if __name == '__main__'，报告里面才有内容，参照run_test.py；以下两种方法均可用
if __name__ == '__main__':
    # unittest.main()
    testunit = unittest.TestSuite()
    #testunit.addTest(Register('test_register_all_null'))
    testunit.addTest(Register('test_register_id_exist'))
    fp = open("result-test.html",'wb')
    runner = HTMLTestRunner(stream=fp, title='test result', description='result')
    runner.run(testunit)
    fp.close()
'''
'''
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(Register)
    filename = "./test-resport-0516.html"
    f = open(filename, 'wb')
    runner = HTMLTestRunner(stream=f, title='Report', description='test', verbosity=2)
    result = runner.run(suite)
    print result.success_count, result.testsRun, result.failure_count
'''