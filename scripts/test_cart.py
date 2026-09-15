import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from base.get_driver import GetDriver
from base.base_case import BaseCase
from page.page_product import PageProduct
from page.page_cart import PageCart
from common.flows import login
from tools.read_json import get_data
from tools.case_doc import case_doc
from tools.price import format_price
from parameterized import parameterized


class TestCart(BaseCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.product = PageProduct(cls.driver)
        cls.cart = PageCart(cls.driver)

    def setUp(self):
        super().setUp()
        login(self.driver)

    @parameterized.expand(get_data("cart"), doc_func=case_doc)
    def test_cart(self, index, qty):
        """购物车合计：加购 N 件后合计等于单价 × 数量"""
        unit = self.product.page_get_product_price(index)

        for _ in range(qty):
            self.product.page_add_cart(index)

        self.cart.page_click_nav_cart()
        total = self.cart.page_get_cart_total()
        self.assertEqual(total, format_price(unit * qty))

    def test_cart_qty_change(self):
        """购物车数量：加减按钮联动数量变化"""
        self.product.page_add_cart(0)
        self.cart.page_click_nav_cart()

        self.cart.page_click_qty_plus()
        self.assertEqual(self.cart.page_get_qty(), "2")

        self.cart.page_click_qty_minus()
        self.assertEqual(self.cart.page_get_qty(), "1")

    def test_cart_delete(self):
        """购物车删除：删除商品后购物车为空"""
        self.product.page_add_cart(0)
        self.cart.page_click_nav_cart()

        self.cart.page_click_del()
        self.assertTrue(self.cart.page_is_cart_empty())

    def test_cart_clear(self):
        """购物车清空：一键清空后购物车为空"""
        self.product.page_add_cart(0)
        self.cart.page_click_nav_cart()

        self.cart.page_click_clear()
        self.assertTrue(self.cart.page_is_cart_empty())


def tearDownModule():
    GetDriver().quit_driver()


if __name__ == "__main__":
    unittest.main(verbosity=2)