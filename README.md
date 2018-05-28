# APITest
## 代码组成
Python+unittest+HTMLTestRunner+xlrd+email+logging
## 目录结构
common：提取公共方法，封装成模块</br>
data：保存测试数据，这里是Excel</br>
interface：接口测试用例</br>
report：测试报告（暂未用）</br>
result：保存测试结果，每次执行脚本生成一个子目录，目录下包括测试报告、日志</br>
config.ini：配置文件，提取可能动态修改的参数</br>
readConfig.py：读取config.ini配置文件的值对</br>
run_tests.py：添加测试集，执行所有的测试用例</br>
