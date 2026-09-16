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
        self.shop.page_click_nav_seller_center()

    def test_seller_center_pagination(self):
        """卖家中心：10 家商家分 2 页，首页 6 家"""
        self.assertTrue(self.shop.page_is_on_seller())
        self.assertEqual(self.shop.page_get_seller_count(), 6)
        self.assertIn("共 10 家店铺", self.shop.page_get_seller_title())
        self.assertTrue(self.shop.page_seller_pager_visible())
        self.assertIn("共 10 条", self.shop.page_get_seller_pager_info())
        self.assertIn("1/2 页", self.shop.page_get_seller_pager_info())

    def test_seller_center_page2(self):
        """卖家中心：第二页展示剩余 4 家，末位为生活优选超市"""
        self.shop.page_click_seller_page(2)
        self.assertEqual(self.shop.page_get_seller_count(), 4)
        names = self.shop.page_get_seller_names()
        self.assertEqual(names[0], "戴尔旗舰店")
        self.assertEqual(names[-1], "淘淘生活优选超市")

    def test_seller_center_shop_order(self):
        """卖家中心：首页商家按序展示，首位 Apple 末位索尼"""
        names = self.shop.page_get_seller_names()
        self.assertEqual(names[0], "Apple官方旗舰店")
        self.assertEqual(names[-1], "索尼官方旗舰店")

    def test_seller_center_rank(self):
        """卖家中心：排行榜展示销量 Top5，榜首为生活优选超市"""
        self.assertEqual(self.shop.page_get_rank_count(), 5)
        rank_names = self.shop.page_get_rank_names()
        self.assertEqual(rank_names[0], "淘淘生活优选超市")
        self.assertIn("3,200,000", self.shop.page_get_first_rank_sales())

    def test_seller_center_rank_enter_shop(self):
        """卖家中心：点击排行榜商家进入对应店铺"""
        self.shop.page_click_rank(0)
        self.assertTrue(self.shop.page_is_on_shop())
        self.assertEqual(self.shop.page_get_shop_name(), "淘淘生活优选超市")

    def test_seller_center_type_filter(self):
        """卖家中心：按类型筛选，手机数码 4 家、综合超市 1 家"""
        self.shop.page_click_type("手机数码")
        self.assertEqual(self.shop.page_get_seller_count(), 4)
        self.assertFalse(self.shop.page_seller_pager_visible())

        self.shop.page_click_type("综合超市")
        self.assertEqual(self.shop.page_get_seller_count(), 1)

    def test_seller_center_enter_shop(self):
        """卖家中心：点击商家卡片进入对应店铺页"""
        self.shop.page_click_seller_shop(0)
        self.assertTrue(self.shop.page_is_on_shop())
        self.assertEqual(self.shop.page_get_shop_name(), "Apple官方旗舰店")
        self.assertGreaterEqual(self.shop.page_get_shop_product_count(), 1)

    def test_seller_center_back(self):
        """卖家中心：返回按钮回到商品列表"""
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