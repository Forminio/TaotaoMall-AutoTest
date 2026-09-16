import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from base.get_driver import GetDriver
from base.base_case import BaseCase
from page.page_coupon import PageCoupon
from page.page_modal import PageModal
from page.page_user import PageUser
from page.page_product import PageProduct
from common.flows import login


class TestMyCoupons(BaseCase):
    """我的优惠券"""

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.coupon = PageCoupon(cls.driver)
        cls.modal = PageModal(cls.driver)
        cls.product = PageProduct(cls.driver)
        cls.user = PageUser(cls.driver)

    def setUp(self):
        super().setUp()
        login(self.driver)

    def test_my_coupons_list(self):
        """我的优惠券：共 12 张分 2 页，首页 6 张"""
        self.coupon.page_click_nav_coupons()
        self.assertTrue(self.coupon.page_is_on_coupons())
        self.assertEqual(self.coupon.page_get_coupon_count(), 6)
        self.assertIn("共 12 条", self.coupon.page_get_pager_info())
        self.assertIn("1/2 页", self.coupon.page_get_pager_info())

    def test_my_coupons_page2(self):
        """我的优惠券：第 2 页展示剩余 6 张，含已过期与已使用状态"""
        self.coupon.page_click_nav_coupons()
        self.coupon.page_click_pager_page(2)
        self.assertEqual(self.coupon.page_get_coupon_count(), 6)
        statuses = self.coupon.page_get_coupon_statuses()
        self.assertIn("已过期", statuses)
        self.assertIn("已使用", statuses)

    def test_my_coupons_use(self):
        """我的优惠券：点击「去使用」跳转商品列表"""
        self.coupon.page_click_nav_coupons()
        self.coupon.page_click_use(0)
        self.assertFalse(self.coupon.page_is_on_coupons())
        self.assertEqual(self.product.page_get_product_title(), "热门推荐")

    def test_my_coupons_from_user_center(self):
        """我的优惠券：个人中心菜单入口可进入"""
        self.user.page_click_nav_user_center()
        self.coupon.page_click_uc_my_coupons()
        self.assertTrue(self.coupon.page_is_on_coupons())


class TestMyCouponsReverse(BaseCase):
    """我的优惠券反向用例"""

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.coupon = PageCoupon(cls.driver)
        cls.user = PageUser(cls.driver)

    def setUp(self):
        super().setUp()

    def test_my_coupons_require_login(self):
        """我的优惠券：未登录点击顶栏入口被拦截"""
        self.coupon.page_click_nav_coupons()
        self.assertFalse(self.coupon.page_is_on_coupons())
        self.assertEqual(self.user.page_get_user_info(), "未登录")


def tearDownModule():
    GetDriver().quit_driver()


if __name__ == "__main__":
    unittest.main(verbosity=2)