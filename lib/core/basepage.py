from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from conf.setting import CHROME_PATH,BROWSER_TYPE,EDGE_PATH

options = webdriver.ChromeOptions()
options.add_experimental_option(
    'excludeSwitches', ['enable-logging'])
options.add_experimental_option('detach', True)
class BasePage:
    _BASE_URL = "https://www.baidu.com/"

    def __init__(self, driver=None):
        if driver:
            self.driver = driver
        else:
            if BROWSER_TYPE == 1:
                self.driver = webdriver.Chrome(options=options,service=Service(CHROME_PATH))
                self.driver.implicitly_wait(3)
                self.driver.maximize_window()
            elif BROWSER_TYPE == 2:
                self.driver = webdriver.Edge(service=Service(EDGE_PATH))
                self.driver.implicitly_wait(3)
                self.driver.maximize_window()

        if not self.driver.current_url.startswith("http"):
            self.driver.get(self._BASE_URL)

    # 元素定位，替代八大定位
    def get_element(self, *element):
        try:
            _type = element[0]
            value = element[1]
            if _type == "id" or _type == "ID" or _type == "Id":
                elem = self.driver.find_element(By.ID, value)
            elif _type == "name" or _type == "NAME" or _type == "Name":
                elem = self.driver.find_element(By.NAME, value)
            elif _type == "class" or _type == "CLASS" or _type == "Class":
                elem = self.driver.find_element(By.CLASS_NAME, value)
            elif _type == "link" or _type == "LINK" or _type == "link":
                elem = self.driver.find_element(By.CLASS_NAME, value)
            elif _type == "xpath" or _type == "XPATH" or _type == "Xpath":
                elem = self.driver.find_element(By.XPATH, value)
            elif _type == "css" or _type == "CSS" or _type == "Css":
                elem = self.driver.find_element(By.CSS_SELECTOR, value)
            else:
                raise NameError("Please input correct the type parameter!")
        except Exception:
            raise NameError("This element not found!" + str(element))
        return elem

    # 点击
    def left_click(self, *locator):
        ActionChains(self.driver).click(self.get_element(*locator)).perform()

    # 输入
    def send_text(self, text, *locator):
        return self.get_element(*locator).send_keys(text)

    # 清空
    def clear_text(self, *locator):
        self.get_element(*locator).clear()

    # 切换表单
    def switch_iframe(self, *locator):
        self.driver.swich_to.frame(self.get_element(*locator))

    # 跳出表单
    def default_switch(self):
        return self.driver.switch_to.default_content()

    # 切换窗口
    def switch_window(self, n):
        self.driver.switch_to.window(self.driver.window_handles[n])

    # 用于断言（元素属性、页面标题、当前网址、标签信息）
    def get_attribute_value(self, name, *locator):
        return self.get_element(*locator).get_attribute(name)

    def get_title(self):
        return self.driver.title

    def get_current_url(self):
        return self.driver.current_url

    def get_element_text(self, *locator):
        return self.get_element(*locator).text

    def quit(self):
        return self.driver.quit()

    def wait(self, sec):
        return self.driver.implicitly_wait(sec)
