import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from base.get_driver import GetDriver
from base.base_case import BaseCase
from page.page_modal import PageModal
from tools.read_json import get_data
from tools.case_doc import case_doc
from parameterized import parameterized


class TestFooterLink(BaseCase):
    """页脚信息页"""

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.modal = PageModal(cls.driver)

    def setUp(self):
        super().setUp()

    @parameterized.expand(get_data("footer_link"), doc_func=case_doc)
    def test_footer_link(self, key, title):
        """页脚链接：点击弹出对应信息弹窗，内容非空且可关闭"""
        self.modal.page_click_footer_link(key)

        self.assertTrue(self.modal.page_modal_is_open())
        self.assertEqual(self.modal.page_get_modal_title(), title)
        self.assertTrue(self.modal.page_get_modal_body().strip())

        self.modal.page_click_modal_button("关闭")
        self.assertFalse(self.modal.page_modal_is_open())


class TestAgreement(BaseCase):
    """协议弹窗"""

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.modal = PageModal(cls.driver)

    def setUp(self):
        super().setUp()

    @parameterized.expand(get_data("agreement"), doc_func=case_doc)
    def test_agreement_modal(self, key, title):
        """协议入口：登录/注册页点击协议弹出对应条款弹窗"""
        self.modal.page_click_agreement_link(key)

        self.assertTrue(self.modal.page_modal_is_open())
        self.assertEqual(self.modal.page_get_modal_title(), title)
        self.assertTrue(self.modal.page_get_modal_body().strip())

        self.modal.page_click_modal_button("关闭")
        self.assertFalse(self.modal.page_modal_is_open())


def tearDownModule():
    GetDriver().quit_driver()


if __name__ == "__main__":
    unittest.main(verbosity=2)