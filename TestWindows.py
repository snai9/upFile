
from selenium.webdriver.common.by import By
import time
from tbase import Tbase

class TstWindows(Tbase):
    def click_windows(self):
        self.setup()
        self.driver.get("http://www.baidu.com")
        self.driver.find_element(By.LINK_TEXT, "登录").click()
        original_window = self.driver.current_window_handle
        self.driver.find_element(By.LINK_TEXT, "立即注册").click()
        
        time.sleep(2)  # 等待新窗口加载
        new_window = [window for window in self.driver.window_handles if window != original_window][0]
        self.driver.switch_to.window(new_window)
        self.driver.find_element(By.ID, "TANGRAM__PSP_4__userName").send_keys("sn")
        time.sleep(5)
        self.driver.switch_to.window(original_window)
        time.sleep(5)
                
        self.teardown()

if __name__ == '__main__':
    TstWindows().click_windows()
