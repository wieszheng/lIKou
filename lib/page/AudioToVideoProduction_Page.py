import time
from lib.core.basepage import BasePage


class Login(BasePage):
    _type = "XPATH"
    def click_login(self):
        self.left_click(self._type, '//*[@id="kw"]')
        self.send_text('nihao',self._type, '//*[@id="kw"]')
        self.quit()
if __name__ == '__main__':
    Login().click_login()
