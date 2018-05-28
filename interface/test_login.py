# -*- coding: utf-8 -*-
import sys
import unittest

from APITest_Kary.common.RequestAPI import testAPI
from APITest_Kary.common.ReadExcel import readExcel
import APITest_Kary.readConfig as rc


if sys.getdefaultencoding() != 'utf-8':
    reload(sys)
    sys.setdefaultencoding('utf-8')

localReadConfig = rc.ReadConfig()


class Login(unittest.TestCase):
    """ 测试登录接口，数据从Excel读取 """
    def test_login_all(self):
        """  Excel表格，一行记录为一条用例 """
        # 登录测试用例，设置表格path、工作簿index
        excel_path = localReadConfig.getTestCase("excel_path")
        excel_index = localReadConfig.getTestCase("excel_index")
        excel = readExcel(excel_path, int(excel_index))
        number = excel.getNumber
        name = excel.getName
        # server = excel.getServer
        # route = excel.getRoute
        url = excel.getURL
        method = excel.getMethod
        data = excel.getData
        code = excel.getCode
        row = excel.getRows
        # 下面依次遍历每一列的数据，并合成一组请求数据
        for i in range(0, row - 1):
            api = testAPI(method[i], url[i], data[i])
            apicode = api.getCode()
            apijson = api.getJson()
            # 判断响应状态码是否与预期一致
            if apicode == code[i]:
                print('{}、{}：测试成功。json数据为：{}'.format(number[i], name[i], apijson))
            else:
                print('{}、{}：测试失败'.format(i + 1, name[i]))


if __name__ == '__main__':
    unittest.main(verbosity=2)
