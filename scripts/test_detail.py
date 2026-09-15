import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from base.get_driver import GetDriver
from base.base_case import BaseCase
from page.page_product import PageProduct
from page.page_detail import PageDetail
from common.flows import login
from tools.read_json import get_data
from tools.case_doc import case_doc
from tools.price import parse_price
from parameterized import parameterized


class TestDetail(BaseCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.product = PageProduct(cls.driver)
        cls.detail = PageDetail(cls.driver)

    def setUp(self):
        super().setUp()
        login(self.driver)

    @parameterized.expand(get_data("detail"), doc_func=case_doc)
    def test_detail(self, index, stock):
        """商品详情：名称/价格与列表页一致，库存展示正确"""
        expect_name = self.product.page_get_product_name(index)
        expect_price = self.product.page_get_product_price(index)

        self.product.page_click_product(index)

        self.assertEqual(self.detail.page_get_detail_name(), expect_name)
        self.assertEqual(parse_price(self.detail.page_get_detail_price()), expect_price)
        self.assertIn(stock, self.detail.page_get_detail_stock())


def tearDownModule():
    GetDriver().quit_driver()


if __name__ == "__main__":
    unittest.main(verbosity=2)