import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from base.get_driver import GetDriver
from base.base_case import BaseCase
from page.page_product import PageProduct
from common.flows import login
from tools.read_json import get_data
from tools.case_doc import case_doc
from parameterized import parameterized


# 分类中文名 -> demo 中 data-cat 值
CATEGORY_MAP = {
    "手机数码": "phone", "电脑办公": "computer", "影音娱乐": "audio",
    "智能穿戴": "wearable", "家用电器": "home", "服饰鞋包": "clothes",
    "食品生鲜": "food", "美妆个护": "beauty", "运动户外": "sports",
    "图书文娱": "book",
}


class TestProduct(BaseCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.product = PageProduct(cls.driver)

    def setUp(self):
        super().setUp()
        login(self.driver)

    @parameterized.expand(get_data("product"), doc_func=case_doc)
    def test_product(self, keyword, expect_count):
        """商品分类与搜索：验证命中数量（单页内），无结果返回 0"""
        if keyword in CATEGORY_MAP:
            self.product.page_click_category(CATEGORY_MAP[keyword])
        else:
            self.product.page_search(keyword)

        self.assertEqual(self.product.page_get_product_count(), expect_count)


def tearDownModule():
    GetDriver().quit_driver()


if __name__ == "__main__":
    unittest.main(verbosity=2)