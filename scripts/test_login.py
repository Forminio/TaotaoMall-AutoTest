import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from base.get_driver import GetDriver
from base.base_case import BaseCase
from page.page_login import PageLogin
from page.page_modal import PageModal
from tools.read_json import get_data
from tools.case_doc import case_doc
from parameterized import parameterized


class TestLogin(BaseCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.login = PageLogin(cls.driver)
        cls.modal = PageModal(cls.driver)

    @parameterized.expand(get_data("login"), doc_func=case_doc)
    def test_login(self, username, password, captcha, expect_msg, success):
        """登录功能：正确凭证登录成功，错误凭证弹出对应提示弹窗"""
        page = self.login
        page.page_login(username, password, captcha)

        if success:
            user_info = page.page_get_user_info()
            self.assertIn(username, user_info)
        else:
            self.assertTrue(self.modal.page_modal_is_open(), "登录失败应弹出提示弹窗")
            self.assertIn(expect_msg, self.modal.page_get_modal_body())
            self.modal.page_click_modal_button("确定")
            self.assertFalse(self.modal.page_modal_is_open())

    def test_logout(self):
        """退出登录：登录后出现退出入口，点击后回到未登录态"""
        self.login.page_login("admin", "123456", "8888")
        self.assertTrue(self.login.page_is_login_success(), "登录成功后应出现退出入口")

        self.login.page_click_logout()
        self.assertFalse(self.login.page_is_login_success(), "退出后退出入口应消失")
        self.assertEqual(self.login.page_get_user_info(), "未登录")


def tearDownModule():
    GetDriver().quit_driver()


if __name__ == "__main__":
    unittest.main(verbosity=2)