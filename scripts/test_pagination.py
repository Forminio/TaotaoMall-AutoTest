import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from base.get_driver import GetDriver
from base.base_case import BaseCase
from page.page_product import PageProduct
from common.flows import login


class TestPagination(BaseCase):
    """商品列表分页（450 件商品 · 每页 15 件 · 5 列满行）"""

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
        """分页：全部 450 件分 30 页，首页铺满 15 件"""
        self._open_all()
        self.assertEqual(self.product.page_get_product_count(), 15)
        self.assertEqual(self.product.page_get_page_num_count(), 30)
        self.assertEqual(self.product.page_get_active_page(), "1")
        info = self.product.page_get_page_info()
        self.assertIn("共 450 件商品", info)
        self.assertIn("1/30 页", info)

    def test_pagination_rows_full(self):
        """分页：每页商品数为 5 的整倍数（末行铺满，不留缺行）"""
        self._open_all()
        total_pages = self.product.page_get_page_num_count()
        for page in range(1, total_pages + 1):
            self.product.page_click_page(page)
            self.assertEqual(self.product.page_get_product_count() % 5, 0,
                             "第 %d 页末行未铺满" % page)

    def test_pagination_click_page(self):
        """分页：点击第 2 页后当前页变为 2 且仍铺满 15 件"""
        self._open_all()
        self.product.page_click_page(2)
        self.assertEqual(self.product.page_get_active_page(), "2")
        self.assertEqual(self.product.page_get_product_count(), 15)

    def test_pagination_last_page(self):
        """分页：最后一页（第 30 页）正常展示 15 件"""
        self._open_all()
        self.product.page_click_page(30)
        self.assertEqual(self.product.page_get_active_page(), "30")
        self.assertEqual(self.product.page_get_product_count(), 15)

    def test_pagination_next_prev(self):
        """分页：下一页 / 上一页切换当前页"""
        self._open_all()
        self.product.page_click_next_page()
        self.assertEqual(self.product.page_get_active_page(), "2")
        self.product.page_click_prev_page()
        self.assertEqual(self.product.page_get_active_page(), "1")

    def test_pagination_category_three_pages(self):
        """分页：单个分类含 45 件商品，分 3 页展示"""
        self.product.page_click_category("phone")
        self.assertEqual(self.product.page_get_page_num_count(), 3)
        info = self.product.page_get_page_info()
        self.assertIn("共 45 件商品", info)
        self.assertIn("1/3 页", info)
        # 切到第 3 页仍铺满
        self.product.page_click_page(3)
        self.assertEqual(self.product.page_get_active_page(), "3")
        self.assertEqual(self.product.page_get_product_count(), 15)


def tearDownModule():
    GetDriver().quit_driver()


if __name__ == "__main__":
    unittest.main(verbosity=2)