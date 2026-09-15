import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from base.get_driver import GetDriver
from base.base_case import BaseCase
from page.page_product import PageProduct
from page.page_coupon import PageCoupon
from page.page_address import PageAddress
from page.page_order import PageOrder
from common.flows import login, checkout
from tools.read_json import get_data
from tools.case_doc import case_doc
from tools.price import format_price
from parameterized import parameterized


# 与 demo 页面 COUPONS 保持一致：value -> (门槛, 优惠金额)
COUPON_RULES = {
    "n": (0, 0),
    "a": (5000, 500),
    "b": (3000, 200),
    "c": (1000, 50),
}


class TestCoupon(BaseCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.product = PageProduct(cls.driver)
        cls.coupon = PageCoupon(cls.driver)
        cls.address = PageAddress(cls.driver)
        cls.order = PageOrder(cls.driver)

    def setUp(self):
        """只登录，不加购"""
        super().setUp()
        login(self.driver)

    @parameterized.expand(get_data("coupon"), doc_func=case_doc)
    def test_coupon(self, index, coupon):
        """优惠券：折后金额等于单价减优惠，未达门槛不打折"""
        unit = self.product.page_get_product_price(index)
        threshold, discount = COUPON_RULES[coupon]
        payable = unit - discount if unit >= threshold else unit
        payable = max(0, payable)

        checkout(self.driver, index)
        self.coupon.page_select_coupon(coupon)
        self.address.page_fill_address("张三", "13800138000", "北京市朝阳区建国路88号")
        self.address.page_click_submit()

        self.assertTrue(self.order.page_is_order_success())
        self.assertIn(format_price(payable), self.order.page_get_order_amount())


def tearDownModule():
    GetDriver().quit_driver()


if __name__ == "__main__":
    unittest.main(verbosity=2)