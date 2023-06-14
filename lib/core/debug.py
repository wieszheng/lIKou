class Base:
    def __init__(self, dr):
        self.dr = dr

    def get_url(self, url):
        """
        获取url地址
        :param url:
        :return:
        """
        self.dr.get(url)

    def get_ele(self, loc):
        """
        元素定位
        :param loc:  Example:(By.ID,"kw")
        :return:
        """
        return WebDriverWait(self.dr, 10).until(lambda x: x.find_element(*loc))

    def input_text(self, loc, text):
        """
        文本框输入
        :param loc:
        :param text: 输入内容
        :return:
        """
        self.get_ele(loc).send_keys(text)

    def click(self, loc):
        """
        点击
        :param loc:
        :return:
        """
        self.get_ele(loc).click()

    def into_iframe(self, frame_id):
        """
        切换iframe
        :param frame_id:
        :return:
        """
        self.dr.switch_to.frame(frame_id)

    def leave_iframe(self):
        """
        返回默认的iframe
        :return:
        """
        self.dr.switch_to.default_content()

    def select(self, loc, num):
        """
        下拉列表
        :param loc:
        :param num: select_by_index(num)
        :return:
        """
        ele = self.get_ele(loc)
        Select(ele).select_by_index(num)

    def clear(self, loc):
        """
        清空
        :param loc:
        :return:
        """
        self.get_ele(loc).clear()

    def quit(self):
        """
        关闭浏览器
        :return:
        """
        self.dr.quit()