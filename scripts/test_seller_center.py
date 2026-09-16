import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from base.get_driver import GetDriver
from base.base_case import BaseCase
from page.page_shop import PageShop
from page.page_user import PageUser
from page.page_product import PageProduct
from common.flows import login


class TestSellerCenter(BaseCase):
    """卖家中心"""

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.shop = PageShop(cls.driver)
        cls.user = PageUser(cls.driver)
        cls.product = PageProduct(cls.driver)

    def setUp(self):
        super().setUp()
        login(self.driver)

    def _open_seller_center(self):
        self.shop.page_click_nav_seller_center()
        self.assertTrue(self.shop.page_is_on_seller())

    def test_seller_center_lists_all_shops(self):
        """卖家中心：罗列全部 10 家商家"""
        self._open_seller_center()
        self.assertEqual(self.shop.page_get_seller_count(), 10)
        self.assertIn("共 10 家店铺", self.shop.page_get_seller_title())

    def test_seller_center_shop_order(self):
        """卖家中心：商家按序展示，首位 Apple 末位生活超市"""
        self._open_seller_center()
        names = self.shop.page_get_seller_names()
        self.assertEqual(names[0], "Apple官方旗舰店")
        self.assertEqual(names[-1], "淘淘生活优选超市")

    def test_seller_center_enter_shop(self):
        """卖家中心：点击商家卡片进入对应店铺页"""
        self._open_seller_center()
        self.shop.page_click_seller_shop(0)
        self.assertTrue(self.shop.page_is_on_shop())
        self.assertEqual(self.shop.page_get_shop_name(), "Apple官方旗舰店")
        self.assertGreaterEqual(self.shop.page_get_shop_product_count(), 1)

    def test_seller_center_enter_last_shop(self):
        """卖家中心：点击最后一个商家进入淘淘生活优选超市"""
        self._open_seller_center()
        self.shop.page_click_seller_shop(9)
        self.assertTrue(self.shop.page_is_on_shop())
        self.assertEqual(self.shop.page_get_shop_name(), "淘淘生活优选超市")

    def test_seller_center_back(self):
        """卖家中心：返回按钮回到商品列表"""
        self._open_seller_center()
        self.shop.page_click_seller_back()
        self.assertFalse(self.shop.page_is_on_seller())
        self.assertEqual(self.product.page_get_product_title(), "热门推荐")


class TestSellerCenterReverse(BaseCase):
    """卖家中心反向用例"""

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.shop = PageShop(cls.driver)
        cls.user = PageUser(cls.driver)

    def setUp(self):
        super().setUp()

    def test_seller_center_require_login(self):
        """卖家中心：未登录点击被拦截，仍为未登录状态"""
        self.shop.page_click_nav_seller_center()
        self.assertFalse(self.shop.page_is_on_seller())
        self.assertEqual(self.user.page_get_user_info(), "未登录")


def tearDownModule():
    GetDriver().quit_driver()


if __name__ == "__main__":
    unittest.main(verbosity=2)