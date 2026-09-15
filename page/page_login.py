from base.base import Base
import page


class PageLogin(Base):
    """登录页"""

    def page_click_login_link(self):
        self.base_click(page.login_link)

    def page_input_username(self, username):
        self.base_input(page.login_username, username)

    def page_input_password(self, pwd):
        self.base_input(page.login_password, pwd)

    def page_input_captcha(self, code):
        self.base_input(page.login_captcha, code)

    def page_click_agree(self):
        self.base_click(page.login_agree)

    def page_click_login_btn(self):
        self.base_click(page.login_btn)

    def page_get_login_msg(self):
        return self.base_text(page.login_msg)

    def page_get_user_info(self):
        return self.base_text(page.user_info)

    def page_is_login_success(self):
        return self.base_is_exist(page.logout_link)

    def page_click_logout(self):
        self.base_click(page.logout_link)

    # 业务组装
    def page_login(self, username, pwd, code, agree=True):
        self.page_input_username(username)
        self.page_input_password(pwd)
        self.page_input_captcha(code)
        if agree:
            self.page_click_agree()
        self.page_click_login_btn()