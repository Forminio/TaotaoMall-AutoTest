import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from base.get_driver import GetDriver
from base.base_case import BaseCase
from page.page_user import PageUser
from page.page_order import PageOrder
from page.page_address import PageAddress
from common.flows import login, checkout


class TestUser(BaseCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = PageUser(cls.driver)
        cls.order = PageOrder(cls.driver)
        cls.address = PageAddress(cls.driver)

    def setUp(self):
        super().setUp()
        login(self.driver)

    def test_user_info(self):
        """个人中心：登录后展示当前用户名"""
        info = self.user.page_get_user_info()
        self.assertIn("admin", info)

    def test_orders_empty(self):
        """我的订单：未下单时订单列表为空"""
        self.user.page_click_nav_orders()
        self.assertTrue(self.user.page_is_orders_empty())

    def test_orders_after_order(self):
        """我的订单：下单后能查到对应订单"""
        checkout(self.driver, 0)
        self.address.page_fill_address("张三", "13800138000", "北京市朝阳区")
        self.address.page_click_submit()

        self.order.page_click_view_orders()
        self.assertGreaterEqual(self.user.page_get_order_count(), 1)

    def test_orders_pagination(self):
        """我的订单：连下 4 单后订单列表分 2 页，第 2 页 1 单"""
        for index in range(4):
            checkout(self.driver, index)
            self.address.page_fill_address("张三", "13800138000", "北京市朝阳区建国路88号")
            self.address.page_click_submit()
            self.order.page_click_back_home()

        self.user.page_click_nav_orders()
        self.assertEqual(self.user.page_get_order_count(), 3)
        self.assertIn("1/2 页", self.user.page_get_orders_pager_info())

        self.user.page_click_orders_page(2)
        self.assertEqual(self.user.page_get_order_count(), 1)


def tearDownModule():
    GetDriver().quit_driver()


if __name__ == "__main__":
    unittest.main(verbosity=2)