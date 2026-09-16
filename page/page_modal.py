from selenium.webdriver.common.by import By

from base.base import Base
import page


class PageModal(Base):
    """通用弹窗 / 页脚信息页 / 协议弹窗"""

    def page_modal_is_open(self):
        return self.base_find(page.modal_overlay).is_displayed()

    def page_get_modal_title(self):
        return self.base_text(page.modal_title)

    def page_get_modal_body(self):
        return self.base_text(page.modal_body)

    def page_click_modal_button(self, text):
        """按按钮文本点击弹窗按钮（如「关闭」「取消」「删除」）"""
        for btn in self.base_finds(page.modal_buttons):
            if btn.text.strip() == text:
                btn.click()
                return
        raise AssertionError(f"弹窗中未找到按钮: {text}")

    def page_click_footer_link(self, key):
        """点击页脚链接（about/contact/join/marketing/links）"""
        self.base_click((By.CSS_SELECTOR, f".foot-link[data-foot='{key}']"))

    def page_click_agreement_link(self, key):
        """点击协议链接。

        key 形如 login_agreement / login_privacy / reg_agreement / reg_privacy；
        注册页的协议链接需要先切到注册页再点击。
        """
        if key.startswith("reg"):
            self.base_click(page.nav_register)
        locator = {
            "login_agreement": page.login_agreement_link,
            "login_privacy": page.login_privacy_link,
            "reg_agreement": page.reg_agreement_link,
            "reg_privacy": page.reg_privacy_link,
        }[key]
        self.base_click(locator)