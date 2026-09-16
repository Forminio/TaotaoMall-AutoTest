import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from base.get_driver import GetDriver
from base.base_case import BaseCase
from page.page_product import PageProduct
from common.flows import login


class TestPagination(BaseCase):
    """商品列表分页"""

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.product = PageProduct(cls.driver)

    def setUp(self):
        super().setUp()
        login(self.driver)

    def _open_all(self):
        self.product.page_click_category("all")

    def test_pagination_total_and_pages(self):
        """分页：全部 40 件分 4 页，首页展示 12 件"""
        self._open_all()
        self.assertEqual(self.product.page_get_product_count(), 12)
        self.assertEqual(self.product.page_get_page_num_count(), 4)
        self.assertEqual(self.product.page_get_active_page(), "1")
        info = self.product.page_get_page_info()
        self.assertIn("共 40 件商品", info)
        self.assertIn("1/4 页", info)

    def test_pagination_click_page(self):
        """分页：点击第 2 页后当前页变为 2"""
        self._open_all()
        self.product.page_click_page(2)
        self.assertEqual(self.product.page_get_active_page(), "2")
        self.assertEqual(self.product.page_get_product_count(), 12)

    def test_pagination_last_page(self):
        """分页：最后一页展示剩余 4 件商品"""
        self._open_all()
        self.product.page_click_page(4)
        self.assertEqual(self.product.page_get_active_page(), "4")
        self.assertEqual(self.product.page_get_product_count(), 4)

    def test_pagination_next_prev(self):
        """分页：下一页 / 上一页切换当前页"""
        self._open_all()
        self.product.page_click_next_page()
        self.assertEqual(self.product.page_get_active_page(), "2")
        self.product.page_click_prev_page()
        self.assertEqual(self.product.page_get_active_page(), "1")

    def test_pagination_single_page_category(self):
        """分页：单页分类仅 1 页且无法跨页"""
        self.product.page_click_category("phone")
        self.assertEqual(self.product.page_get_page_num_count(), 1)
        info = self.product.page_get_page_info()
        self.assertIn("共 4 件商品", info)
        self.assertIn("1/1 页", info)


def tearDownModule():
    GetDriver().quit_driver()


if __name__ == "__main__":
    unittest.main(verbosity=2)