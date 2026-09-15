from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Base:
    def __init__(self, driver):
        self.driver = driver

    # 查找元素方法 封装
    def base_find(self, loc, timeout=10, poll=0.5):
        return WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll).until(
            lambda d: d.find_element(*loc)
        )

    # 查找多个元素
    def base_finds(self, loc, timeout=30, poll=0.5):
        WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll).until(
            lambda d: len(d.find_elements(*loc)) > 0
        )
        return self.driver.find_elements(*loc)

    # 点击元素
    def base_click(self, loc):
        self.base_find(loc).click()

    # JS 强制点击
    def base_js_click(self, loc):
        el = self.base_find(loc)
        self.driver.execute_script("arguments[0].click();", el)

    # 输入元素
    def base_input(self, loc, input_keys):
        el = self.base_find(loc)
        el.clear()
        el.send_keys(input_keys)

    # 获取文本信息
    def base_text(self, loc):
        return self.base_find(loc).text

    # 获取属性
    def base_attr(self, loc, attr):
        return self.base_find(loc).get_attribute(attr)

    # 获取 value
    def base_value(self, loc):
        return self.base_find(loc).get_attribute("value")

    # 判断元素是否存在
    def base_is_exist(self, loc):
        try:
            self.driver.find_element(*loc)
            return True
        except Exception:
            return False

    # 切换到 iframe
    def base_switch_iframe(self, loc):
        self.driver.switch_to.frame(self.base_find(loc))

    # 切回主页面
    def base_switch_default(self):
        self.driver.switch_to.default_content()

    # 切换窗口
    def base_switch_window(self, handle):
        self.driver.switch_to.window(handle)

    # 获取 alert
    def base_get_alert(self):
        return WebDriverWait(self.driver, 10).until(EC.alert_is_present())

    # 刷新
    def base_refresh(self):
        self.driver.refresh()

    # 打开 URL
    def base_get(self, url):
        self.driver.get(url)

    # 执行 JS
    def base_execute_script(self, script, *args):
        return self.driver.execute_script(script, *args)