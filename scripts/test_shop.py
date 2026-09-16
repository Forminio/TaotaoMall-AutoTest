import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from base.get_driver import GetDriver
from base.base_case import BaseCase
from page.page_product import PageProduct
from page.page_detail import PageDetail
from page.page_shop import PageShop
from page.page_user import PageUser
from common.flows import login
from tools.read_json import get_data
from tools.case_doc import case_doc
from parameterized import parameterized


class TestShop(BaseCase):
    """店铺 / 商家详情页"""

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.product = PageProduct(cls.driver)
        cls.detail = PageDetail(cls.driver)
        cls.shop = PageShop(cls.driver)

    def setUp(self):
        super().setUp()
        login(self.driver)

    def test_shop_from_seller_center(self):
        """卖家中心：从商家列表进入店铺并展示店铺商品"""
        self.shop.page_click_nav_seller_center()
        self.assertTrue(self.shop.page_is_on_seller())
        self.shop.page_click_seller_shop(0)
        self.assertTrue(self.shop.page_is_on_shop())
        self.assertEqual(self.shop.page_get_shop_name(), "Apple官方旗舰店")
        self.assertGreaterEqual(self.shop.page_get_shop_product_count(), 1)

    def test_shop_from_detail(self):
        """店铺页：从商品详情「进入店铺」正确跳转"""
        self.product.page_click_product(0)
        self.assertIn("Apple", self.shop.page_get_detail_shop_name())
        self.shop.page_click_shop_link()
        self.assertTrue(self.shop.page_is_on_shop())
        self.assertEqual(self.shop.page_get_shop_name(), "Apple官方旗舰店")

    def test_shop_back_to_home(self):
        """店铺页：返回按钮回到商品列表"""
        self.shop.page_click_nav_seller_center()
        self.shop.page_click_seller_shop(0)
        self.assertTrue(self.shop.page_is_on_shop())
        self.shop.page_click_shop_back()
        self.assertFalse(self.shop.page_is_on_shop())
        self.assertEqual(self.product.page_get_product_title(), "热门推荐")

    @parameterized.expand(get_data("shop"), doc_func=case_doc)
    def test_shop_info(self, shop_id, name, rating, main, location, since, product_count):
        """店铺详情：名称/评分/主营/所在地/开店时间/商品数量正确"""
        # showShop 与页面点击「进入店铺」触发的是同一渲染逻辑，此处用于覆盖全部商家
        self.driver.execute_script("showShop(%d);" % shop_id)

        self.assertEqual(self.shop.page_get_shop_name(), name)
        stats = self.shop.page_get_shop_stats()
        self.assertIn("评分 " + rating, stats)
        self.assertIn(main, stats)
        self.assertIn(location, stats)
        self.assertIn("开店 " + since, stats)
        self.assertTrue(self.shop.page_get_shop_desc().strip())
        self.assertEqual(self.shop.page_get_shop_product_count(), product_count)


class TestShopReverse(BaseCase):
    """店铺页反向用例"""

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.shop = PageShop(cls.driver)
        cls.user = PageUser(cls.driver)

    def setUp(self):
        super().setUp()

    def test_shop_require_login(self):
        """店铺页：未登录点击「卖家中心」被拦截，仍为未登录状态"""
        self.shop.page_click_nav_seller_center()
        self.assertFalse(self.shop.page_is_on_shop())
        self.assertEqual(self.user.page_get_user_info(), "未登录")


def tearDownModule():
    GetDriver().quit_driver()


if __name__ == "__main__":
    unittest.main(verbosity=2)