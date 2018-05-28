from selenium.webdriver.common.by import By
from Base.Base import Base

class Search_Page(Base):

    def __init__(self, driver):
        Base.__init__(self,driver)
        # 搜索按钮
        self.search_btn = (By.ID, "com.android.settings:id/search")
        # 搜索输入框
        self.search_input = (By.ID, "android:id/search_src_text")
        # 搜索结果列表
        self.search_result = (By.ID, "com.android.settings:id/title")

    def search_text(self, text_value):
        # 搜索内容
        # 点击搜索按钮
        self.click_element(self.search_btn)
        # 定位搜索输入框
        self.input_element(self.search_input, text_value)
        # 获取搜索结果列表
        result_list = self.search_elements(self.search_result, timeout=5)
        return [i.text for i in result_list]