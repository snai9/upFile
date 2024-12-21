import os  # 导入os模块，用于操作系统功能
from selenium import webdriver  # 导入webdriver模块


class Tbase():  # 定义Base类
    def setup(self):  # 设置浏览器环境
        browser = os.getenv("browser")  # 获取环境变量中的浏览器类型
        if browser == 'edge':  # 如果浏览器为Edge
            self.driver = webdriver.Edge()  # 初始化Edge浏览器
        elif browser == 'headless':  # 如果浏览器为无头模式
            options = webdriver.ChromeOptions()  # 创建Chrome选项
            options.add_argument('--headless')  # 添加无头参数
            self.driver = webdriver.Chrome(options=options)  # 初始化无头Chrome浏览器
        else:  # 默认使用Chrome浏览器
            self.driver = webdriver.Chrome()  # 初始化Chrome浏览器
        self.driver.implicitly_wait(5)  # 设置隐式等待时间
        self.driver.maximize_window()  # 最大化浏览器窗口

    def teardown(self):  # 清理操作
        self.driver.quit()  # 关闭浏览器
