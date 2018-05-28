# -*- coding: utf-8 -*-
# 执行测试用例，并生成测试报告
# 使用discover在指定目录下检索文件，并用run方法执行文件里的用例
import unittest
from HTMLTestRunner import HTMLTestRunner
import time
import sys
from common.PrintLog import MyLog
from common.SendEmail import Email
import APITest_Kary.readConfig as rc

# 解决：UnicodeDecodeError: 'ascii' codec can't decode byte 0xe8 in position
# 原因：python2.x的默认编码是ascii，而代码中可能由utf-8的字符导致
if sys.getdefaultencoding() != 'utf-8':
    reload(sys)
    sys.setdefaultencoding('utf-8')

# 实例化ReadConfig
localReadConfig = rc.ReadConfig()
# 1)获取测试项目、测试模块名，在报告显示
test_programe = localReadConfig.getTestAbout("test_programe")
test_module = localReadConfig.getTestAbout("test_module")
# 2)判断邮件开关，on_off为0发送，为1不发送
on_off = localReadConfig.getEmail("on_off")

# 实例化Log模块的MyLog类
log = MyLog.get_log()
logger = log.logger

# 实例化Email模块的Email类
email = Email()

# 测试用例路径
sys.path.append('./interface')
test_dir = './interface'


# 遍历所有的用例，放入一个列表中
def all_case():
    discover = unittest.defaultTestLoader.discover(test_dir, pattern='test_*.py', top_level_dir=None)
    print(discover)
    return discover


# 生成测试报告，保存至Log()生成的文件夹下，及./result/now/
if __name__ == "__main__":
    filepath = log.logPath
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = filepath + '/' + now + '_result.html'
    try:
        log.logger.info("******** TEST START *********")
        f = open(filename, 'wb')
        runner = HTMLTestRunner(stream=f, title=test_programe + ' ' + test_module + ' Test Report',
                            description='Implementation Example with:')
        runner.run(all_case())
        f.close()
    except Exception as ex:
        logger.error(str(ex))
    finally:
        # 根据开关，判断是否发送邮件（附件为执行脚本时生成的文件夹zip）
        if int(on_off) == 0:
            email.send_email()
        elif int(on_off) == 1:
            logger.info("Doesn't send email to developer.")
        else:
            logger.info("Unknow state.")
        logger.info("******** TEST END *********")
