import time
from selenium.webdriver.common.by import By
from tbase import Tbase

class TstWindows(Tbase):
    def click_windows(self):
        self.setup()  # 设置驱动和基础环境
        self.driver.get("http://www.baidu.com")  # 打开百度首页
        self.driver.find_element(By.LINK_TEXT, "登录").click()  # 点击登录链接
        original_window = self.driver.current_window_handle  # 获取当前窗口句柄
        self.driver.find_element(By.LINK_TEXT, "立即注册").click()  # 点击立即注册链接
        time.sleep(2)  # 等待新窗口加载
        new_window = [
            # 获取新打开的窗口句柄
            window for window in self.driver.window_handles if window != original_window][0]
        self.driver.switch_to.window(new_window)  # 切换到新窗口
        self.driver.find_element(
            By.ID, "TANGRAM__PSP_4__userName").send_keys("sn")  # 在注册页面输入用户名
        time.sleep(5)  # 等待操作完成
        self.driver.switch_to.window(original_window)  # 切换回原窗口
        time.sleep(5)  # 等待操作完成
        self.teardown()  # 清理环境

if __name__ == '__main__':
    TstWindows().click_windows()  # 执行测试
