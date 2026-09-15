from base.base import Base
import page


class PageRegister(Base):
    """注册页"""

    def page_click_nav_register(self):
        self.base_click(page.nav_register)

    def page_click_goto_register(self):
        """从登录页跳转到注册页"""
        self.base_click(page.goto_register_link)

    def page_input_username(self, username):
        self.base_input(page.reg_username, username)

    def page_input_password(self, pwd):
        self.base_input(page.reg_password, pwd)

    def page_input_confirm(self, confirm):
        self.base_input(page.reg_confirm, confirm)

    def page_input_phone(self, phone):
        self.base_input(page.reg_phone, phone)

    def page_click_agree(self):
        self.base_click(page.reg_agree)

    def page_click_register_btn(self):
        self.base_click(page.reg_btn)

    def page_get_register_msg(self):
        return self.base_text(page.reg_msg)

    def page_get_user_info(self):
        return self.base_text(page.user_info)

    def page_is_register_success(self):
        """注册成功后自动登录并进入商品列表页"""
        return self.base_is_exist(page.product_box)

    def page_back_to_login(self):
        self.base_click(page.back_login_link)

    # 业务组装
    def page_register(self, username, pwd, confirm, phone, agree=True):
        self.page_input_username(username)
        self.page_input_password(pwd)
        self.page_input_confirm(confirm)
        self.page_input_phone(phone)
        if agree:
            self.page_click_agree()
        self.page_click_register_btn()