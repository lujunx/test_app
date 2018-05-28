import sys, os
sys.path.append(os.getcwd())

from appium import webdriver
from Page.search_page1 import Search_Page
import pytest

class Test_Search:
    def setup_class(self):
        # 声明driver
        # server 启动参数
        desired_caps = {}
        # 设备信息
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.1'
        desired_caps['deviceName'] = '192.168.56.101:5555'
        desired_caps['noReset'] = 'true'
        # app的信息
        desired_caps['appPackage'] = 'com.android.settings'
        desired_caps['appActivity'] = '.Settings'
        desired_caps['unicodeKeyboard'] = True
        desired_caps['resetKeyboard'] = True
        # 声明我们的driver对象
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

        # 实例化搜索页面类
        self.search_obj = Search_Page(self.driver)

    def teardown_class(self):
        # 退出driver
        self.driver.quit()

    @pytest.mark.parametrize("input_data,expect_data",[("1","休眠")])
    def test_search(self, input_data, expect_data):
        data_result = self.search_obj.search_text(input_data)
        assert expect_data in data_result