import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.get_driver import GetDriver
from base.base_case import BaseCase
from page.page_product import PageProduct
from page.page_cart import PageCart
from page.page_user import PageUser
from page.page_shop import PageShop
from page.page_messages import PageMessages
from common.flows import login
from tools.case_doc import case_doc
from parameterized import parameterized
import page


def assert_toast(driver, expect_text):
    """等待 toast 提示出现并校验文案"""
    toast = WebDriverWait(driver, 3, 0.1).until(
        EC.presence_of_element_located(page.toast))
    assert toast.text == expect_text, f"toast 文案不符: {toast.text}"


NAV_BLOCK_CASES = [
    ("nav_cart", lambda d: PageCart(d).page_click_nav_cart()),
    ("nav_orders", lambda d: PageUser(d).page_click_nav_orders()),
    ("nav_user_center", lambda d: PageUser(d).page_click_nav_user_center()),
    ("nav_seller_center", lambda d: PageShop(d).page_click_nav_seller_center()),
    ("nav_messages", lambda d: PageMessages(d).page_click_nav_messages()),
    ("nav_customer_service", lambda d: PageMessages(d).page_click_nav_customer_service()),
]


class TestUnauthorized(BaseCase):
    """未登录权限控制"""

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.product = PageProduct(cls.driver)
        cls.user = PageUser(cls.driver)

    def setUp(self):
        super().setUp()

    @parameterized.expand(NAV_BLOCK_CASES, doc_func=case_doc)
    def test_nav_blocked_without_login(self, name, action):
        """未登录拦截：点击各功能入口弹出「请先登录」"""
        action(self.driver)
        assert_toast(self.driver, "请先登录")
        self.assertEqual(self.user.page_get_user_info(), "未登录")

    def test_browse_products_without_login(self):
        """未登录浏览：可以切换分类查看商品列表"""
        self.product.page_click_category("phone")
        self.assertEqual(self.product.page_get_product_count(), 4)

    def test_add_cart_blocked_without_login(self):
        """未登录拦截：点击加入购物车弹出「请先登录」"""
        self.product.page_click_category("all")
        self.product.page_add_cart(0)
        assert_toast(self.driver, "请先登录")
        self.assertEqual(self.user.page_get_user_info(), "未登录")

    def test_buy_now_blocked_without_login(self):
        """未登录拦截：详情页立即购买弹出「请先登录」"""
        self.product.page_click_category("all")
        self.product.page_click_product(0)
        self.driver.find_element(*page.detail_buy_now).click()
        assert_toast(self.driver, "请先登录")


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