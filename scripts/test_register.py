import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from base.get_driver import GetDriver
from base.base_case import BaseCase
from page.page_register import PageRegister
from tools.read_json import get_data
from tools.case_doc import case_doc
from parameterized import parameterized


class TestRegister(BaseCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.register = PageRegister(cls.driver)

    def setUp(self):
        super().setUp()
        self.register.page_click_nav_register()

    @parameterized.expand(get_data("register"), doc_func=case_doc)
    def test_register(self, username, password, confirm, phone, expect_msg, agree, success):
        """注册功能：验证表单校验规则，合法数据注册成功并自动登录"""
        self.register.page_register(username, password, confirm, phone, agree)

        if success:
            user_info = self.register.page_get_user_info()
            self.assertIn(username, user_info)
            self.assertTrue(self.register.page_is_register_success(),
                            "注册成功后应自动登录并进入商品列表页")
        else:
            msg = self.register.page_get_register_msg()
            self.assertEqual(msg, expect_msg)


def tearDownModule():
    GetDriver().quit_driver()


if __name__ == "__main__":
    unittest.main(verbosity=2)