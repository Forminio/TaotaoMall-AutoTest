import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from base.get_driver import GetDriver
from base.base_case import BaseCase
from page.page_product import PageProduct
from page.page_cart import PageCart
from page.page_user import PageUser
from page.page_shop import PageShop
from page.page_messages import PageMessages
from page.page_modal import PageModal
from common.flows import login
from tools.case_doc import case_doc
from parameterized import parameterized
import page


def assert_login_alert(driver, expect_text="请先登录"):
    """未登录拦截：断言弹出 div 提示弹窗且文案正确，并关闭弹窗"""
    modal = PageModal(driver)
    assert modal.page_modal_is_open(), "应弹出「请先登录」提示弹窗"
    assert expect_text in modal.page_get_modal_body(), "弹窗文案不符"
    modal.page_click_modal_button("确定")


class TestUnauthorized(BaseCase):
    """未登录权限控制"""

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.product = PageProduct(cls.driver)
        cls.user = PageUser(cls.driver)

    def setUp(self):
        super().setUp()

    @parameterized.expand([
        ("nav_cart",), ("nav_orders",), ("nav_user_center",),
        ("nav_seller_center",), ("nav_messages",), ("nav_customer_service",),
        ("nav_coupons",), ("nav_address",),
    ], doc_func=case_doc)
    def test_nav_blocked_without_login(self, name):
        """未登录拦截：点击各功能入口弹出「请先登录」弹窗"""
        actions = {
            "nav_cart": lambda: PageCart(self.driver).page_click_nav_cart(),
            "nav_orders": lambda: PageUser(self.driver).page_click_nav_orders(),
            "nav_user_center": lambda: PageUser(self.driver).page_click_nav_user_center(),
            "nav_seller_center": lambda: PageShop(self.driver).page_click_nav_seller_center(),
            "nav_messages": lambda: PageMessages(self.driver).page_click_nav_messages(),
            "nav_customer_service": lambda: PageMessages(self.driver).page_click_nav_customer_service(),
            "nav_coupons": lambda: self.driver.find_element(*page.nav_coupons).click(),
            "nav_address": lambda: self.driver.find_element(*page.nav_address).click(),
        }
        actions[name]()
        assert_login_alert(self.driver)
        self.assertEqual(self.user.page_get_user_info(), "未登录")

    def test_browse_products_without_login(self):
        """未登录浏览：可以切换分类查看商品列表"""
        self.product.page_click_category("phone")
        self.assertEqual(self.product.page_get_product_count(), 4)

    def test_add_cart_blocked_without_login(self):
        """未登录拦截：点击加入购物车弹出「请先登录」"""
        self.product.page_click_category("all")
        self.product.page_add_cart(0)
        assert_login_alert(self.driver)
        self.assertEqual(self.user.page_get_user_info(), "未登录")

    def test_buy_now_blocked_without_login(self):
        """未登录拦截：详情页立即购买弹出「请先登录」"""
        self.product.page_click_category("all")
        self.product.page_click_product(0)
        self.driver.find_element(*page.detail_buy_now).click()
        assert_login_alert(self.driver)


class TestRegisterLinkLifecycle(BaseCase):
    """「免费注册」入口生命周期"""

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = PageUser(cls.driver)

    def setUp(self):
        super().setUp()

    def _nav_register_visible(self):
        return self.driver.find_element(*page.nav_register).is_displayed()

    def test_register_link_hidden_after_login(self):
        """顶栏：登录后「免费注册」隐藏，退出登录后恢复"""
        self.assertTrue(self._nav_register_visible())
        login(self.driver)
        self.assertFalse(self._nav_register_visible())

        self.user.page_click_nav_user_center()
        self.user.page_click_uc_logout()
        self.assertTrue(self._nav_register_visible())
        self.assertEqual(self.user.page_get_user_info(), "未登录")


def tearDownModule():
    GetDriver().quit_driver()


if __name__ == "__main__":
    unittest.main(verbosity=2)