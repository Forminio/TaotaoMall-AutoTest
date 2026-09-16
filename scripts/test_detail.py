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


class TestDetailRich(BaseCase):
    """详情页 广告长图 / 分区标签 / 猜你喜欢"""

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.product = PageProduct(cls.driver)
        cls.detail = PageDetail(cls.driver)

    def setUp(self):
        super().setUp()
        login(self.driver)
        self.product.page_click_product(2)

    def test_detail_long_image(self):
        """详情长图：多张同分类网络高清图拼接 + 广告语，仿淘宝商品详情长图"""
        srcs = self.detail.page_long_img_srcs()
        self.assertGreaterEqual(self.detail.page_long_img_count(), 3,
                                "广告长图应由多张图片拼接")
        for src in srcs:
            self.assertTrue(src.startswith("http") and "loremflickr.com" in src,
                            "每张长图应为网络真实图片地址")

    def test_detail_tabs(self):
        """详情分区：默认四条 Tab，默认激活「商品详情」且展示卖点文案"""
        self.assertEqual(self.detail.page_get_tab_count(), 4)
        self.assertEqual(self.detail.page_get_tab_names(),
                         ["商品详情", "使用方法", "免责声明", "猜你喜欢"])
        self.assertEqual(self.detail.page_active_tab(), "商品详情")
        self.assertIn("核心亮点", self.detail.page_get_panel_text())

    def test_detail_tab_switch(self):
        """详情分区：切换「使用方法/免责声明」Tab 展示对应正文"""
        self.detail.page_click_tab("usage")
        self.assertEqual(self.detail.page_active_tab(), "使用方法")
        self.assertIn("使用前请阅读", self.detail.page_get_panel_text())

        self.detail.page_click_tab("disclaimer")
        self.assertEqual(self.detail.page_active_tab(), "免责声明")
        self.assertIn("免责声明", self.detail.page_get_panel_text())

    def test_detail_recommend_list(self):
        """详情推荐：「猜你喜欢」展示 5 条同分类热门推荐"""
        self.detail.page_click_tab("recommend")
        self.assertEqual(self.detail.page_active_tab(), "猜你喜欢")
        self.assertIn("看了又看", self.detail.page_get_reco_head())
        self.assertEqual(self.detail.page_get_reco_count(), 5)

    def test_detail_recommend_jump(self):
        """详情推荐：点击推荐卡片跳转到对应商品详情"""
        self.detail.page_click_tab("recommend")
        first_name = self.detail.page_get_reco_names()[0]
        self.detail.page_click_reco(0)
        self.assertEqual(self.detail.page_get_detail_name(), first_name)


def tearDownModule():
    GetDriver().quit_driver()


if __name__ == "__main__":
    unittest.main(verbosity=2)