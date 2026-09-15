import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from base.get_driver import GetDriver
from base.base_case import BaseCase
from page.page_address import PageAddress
from page.page_order import PageOrder
from common.flows import login, checkout
from tools.read_json import get_data
from tools.case_doc import case_doc
from parameterized import parameterized


class TestAddress(BaseCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.address = PageAddress(cls.driver)
        cls.order = PageOrder(cls.driver)

    def setUp(self):
        super().setUp()
        login(self.driver)
        checkout(self.driver, 0)

    @parameterized.expand(get_data("address"), doc_func=case_doc)
    def test_address(self, receiver, phone, address, success):
        """收货地址校验：合法地址提交成功，非法输入停留在结算页"""
        self.address.page_fill_address(receiver, phone, address)
        self.address.page_click_submit()

        if success:
            self.assertTrue(self.order.page_is_order_success(),
                            "提交成功后应进入下单成功页")
        else:
            self.assertTrue(self.address.page_is_on_checkout(),
                            "提交失败后应停留在结算页")


def tearDownModule():
    GetDriver().quit_driver()


if __name__ == "__main__":
    unittest.main(verbosity=2)