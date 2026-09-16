import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from selenium.webdriver.support.wait import WebDriverWait

from base.get_driver import GetDriver
from base.base_case import BaseCase
from page.page_banner import PageBanner


class TestBanner(BaseCase):
    """首页广告轮播"""

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.banner = PageBanner(cls.driver)

    def setUp(self):
        super().setUp()

    def test_banner_render(self):
        """广告轮播：加载后展示 4 帧与 4 个圆点，默认第 1 帧激活"""
        self.assertTrue(self.banner.page_banner_visible())
        self.assertEqual(self.banner.page_get_banner_count(), 4)
        self.assertEqual(self.banner.page_get_dot_count(), 4)
        self.assertEqual(self.banner.page_get_active_index(), "0")

    def test_banner_auto_switch(self):
        """广告轮播：3 秒自动切换到下一帧"""
        WebDriverWait(self.driver, 8, 0.5).until(
            lambda d: self.banner.page_get_active_index() != "0",
            message="轮播 8 秒内未自动切换")
        self.assertEqual(self.banner.page_get_active_index(), "1")

    def test_banner_dot_switch(self):
        """广告轮播：点击圆点切换到对应帧"""
        self.banner.page_click_dot(3)
        self.assertEqual(self.banner.page_get_active_index(), "3")
        self.banner.page_click_dot(1)
        self.assertEqual(self.banner.page_get_active_index(), "1")

    def test_banner_close(self):
        """广告轮播：点击 X 后整条广告消失"""
        self.banner.page_close_banner()
        self.assertFalse(self.banner.page_banner_visible())


def tearDownModule():
    GetDriver().quit_driver()


if __name__ == "__main__":
    unittest.main(verbosity=2)