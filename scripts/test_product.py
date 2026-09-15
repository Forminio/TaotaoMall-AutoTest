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
        """商品搜索与分类：验证命中数量，无结果返回 0"""
        if keyword in ["手机数码", "电脑办公", "影音娱乐", "智能穿戴", "家用电器", "全部"]:
            cat_map = {
                "手机数码": "phone", "电脑办公": "computer",
                "影音娱乐": "audio", "智能穿戴": "wearable",
                "家用电器": "home", "全部": "all"
            }
            self.product.page_click_category(cat_map[keyword])
        else:
            self.product.page_search(keyword)

        count = self.product.page_get_product_count()
        if expect_count == 0:
            self.assertEqual(count, 0)
        else:
            self.assertGreaterEqual(count, expect_count)


def tearDownModule():
    GetDriver().quit_driver()


if __name__ == "__main__":
    unittest.main(verbosity=2)