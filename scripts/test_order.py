import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from base.get_driver import GetDriver
from base.base_case import BaseCase
from page.page_product import PageProduct
from page.page_address import PageAddress
from page.page_order import PageOrder
from common.flows import login, checkout
from tools.read_json import get_data
from tools.case_doc import case_doc
from tools.price import format_price
from parameterized import parameterized


class TestOrder(BaseCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.product = PageProduct(cls.driver)
        cls.address = PageAddress(cls.driver)
        cls.order = PageOrder(cls.driver)

    def setUp(self):
        """只登录，不加购"""
        super().setUp()
        login(self.driver)

    @parameterized.expand(get_data("order"), doc_func=case_doc)
    def test_order(self, receiver, phone, address, remark, index):
        """完整下单流程：加购结算后下单成功，金额等于商品单价"""
        unit = self.product.page_get_product_price(index)

        checkout(self.driver, index)
        self.address.page_fill_address(receiver, phone, address, remark)
        self.address.page_click_submit()

        self.assertTrue(self.order.page_is_order_success())
        self.assertEqual(self.order.page_get_order_receiver(), receiver)
        self.assertIn(format_price(unit), self.order.page_get_order_amount())


def tearDownModule():
    GetDriver().quit_driver()


if __name__ == "__main__":
    unittest.main(verbosity=2)