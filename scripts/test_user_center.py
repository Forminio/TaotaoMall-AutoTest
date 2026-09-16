import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from base.get_driver import GetDriver
from base.base_case import BaseCase
from page.page_user import PageUser
from page.page_address import PageAddress
from page.page_coupon import PageCoupon
from common.flows import login


class TestUserCenter(BaseCase):
    """个人中心"""

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = PageUser(cls.driver)
        cls.address = PageAddress(cls.driver)
        cls.coupon = PageCoupon(cls.driver)

    def setUp(self):
        super().setUp()
        login(self.driver)

    def _open_user_center(self):
        self.user.page_click_nav_user_center()
        self.assertTrue(self.user.page_is_on_user_center())

    def test_user_center_name(self):
        """个人中心：登录后展示当前用户名"""
        self._open_user_center()
        self.assertEqual(self.user.page_get_uc_name(), "admin")

    def test_user_center_stats(self):
        """个人中心：初始订单数 0，地址数 8"""
        self._open_user_center()
        self.assertEqual(self.user.page_get_uc_order_count(), "0")
        self.assertEqual(self.user.page_get_uc_addr_count(), "8")

    def test_user_center_nav_orders(self):
        """个人中心：点击订单统计跳转我的订单"""
        self._open_user_center()
        self.user.page_click_uc_nav_orders()
        self.assertTrue(self.user.page_is_on_orders())

    def test_user_center_my_orders(self):
        """个人中心：菜单「我的订单」跳转订单页"""
        self._open_user_center()
        self.user.page_click_uc_my_orders()
        self.assertTrue(self.user.page_is_on_orders())

    def test_user_center_nav_address(self):
        """个人中心：点击地址统计跳转地址管理"""
        self._open_user_center()
        self.user.page_click_uc_nav_address()
        self.assertTrue(self.address.page_is_on_manage())

    def test_user_center_manager_address(self):
        """个人中心：菜单「管理收货地址」跳转地址管理"""
        self._open_user_center()
        self.user.page_click_uc_manager_address()
        self.assertTrue(self.address.page_is_on_manage())

    def test_user_center_my_coupons(self):
        """个人中心：菜单「我的优惠券」跳转优惠券页"""
        self._open_user_center()
        self.coupon.page_click_uc_my_coupons()
        self.assertTrue(self.coupon.page_is_on_coupons())

    def test_user_center_logout(self):
        """个人中心：退出登录回到未登录态"""
        self._open_user_center()
        self.user.page_click_uc_logout()
        self.assertFalse(self.user.page_is_on_user_center())
        self.assertEqual(self.user.page_get_user_info(), "未登录")


class TestUserCenterReverse(BaseCase):
    """个人中心反向用例"""

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = PageUser(cls.driver)

    def setUp(self):
        super().setUp()

    def test_user_center_require_login(self):
        """个人中心：未登录点击「我的淘宝」被拦截"""
        self.user.page_click_nav_user_center()
        self.assertFalse(self.user.page_is_on_user_center())
        self.assertEqual(self.user.page_get_user_info(), "未登录")


def tearDownModule():
    GetDriver().quit_driver()


if __name__ == "__main__":
    unittest.main(verbosity=2)