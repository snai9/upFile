import os  # 导入os模块，用于操作系统功能
import time  # 导入time模块，用于时间相关操作
import logging
from selenium import webdriver  # 导入webdriver模块
from selenium.webdriver.common.by import By  # 导入定位元素的By类
from selenium.webdriver.support import expected_conditions as EC  # 导入预期条件模块
from selenium.webdriver.support.ui import WebDriverWait  # 导入WebDriverWait类，用于等待元素
from selenium.common.exceptions import NoSuchElementException, TimeoutException  # 导入异常类


class Base():  # 定义Base类
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


class TestAlert(Base):  # 定义TestAlert类，继承Base类
    def test_upload(self):  # 定义测试上传的方法
        self.setup()  # 调用setup方法，初始化浏览器
        self.driver.get("https://image.baidu.com/")  # 打开百度图片网站

        # 等待上传按钮可见
        try:
            WebDriverWait(self.driver, 10).until(  # 等待相机按钮可见
                EC.visibility_of_element_located(
                    (By.XPATH, "//*/form/span[2]/i"))  # 相机按钮的XPath
            ).click()  # 点击相机按钮

            print("点击相机成功")  # 打印成功信息

            WebDriverWait(self.driver, 10).until(  # 等待上传按钮可见
                EC.visibility_of_element_located(
                    # 上传按钮的XPath
                    (By.XPATH, "//*/div[3]/div[2]/div[2]/div/div[1]"))
            ).click()  # 点击上传按钮
            time.sleep(2)  # 暂停2秒
            result = os.system(r"D:\\python学习\\自动化测试\\upfile.exe")
            if result == 0:
                logging.error("点击上传成功")  # 打印成功信息
            else:
                logging.error(f"上传失败，错误代码: {result}")

        except NoSuchElementException as e:
            logging.error(f"Element not found: {e}")
        except TimeoutException as e:
            logging.error(f"Timeout error: {e}")
        except Exception as e:  # 捕获异常
            logging.error(f"Error occurred: {e}")  # 打印错误信息
            logging.error(f"Exception type: {type(e)}")
            logging.error(f"Exception args: {e.args}")

        finally:
            time.sleep(10)
            print("Calling teardown...")
            self.teardown()  # 清理操作


if __name__ == "__main__":  # 主程序入口
    logging.basicConfig(level=logging.ERROR,  # 设置日志级别
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    filename='test.log',  # 日志文件名
                    filemode='a')  # 追加模式
    test = TestAlert()  # 实例化TestAlert类
    test.test_upload()  # 调用测试上传的方法
