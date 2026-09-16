import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from base.get_driver import GetDriver
from base.base_case import BaseCase
from page.page_address import PageAddress
from common.flows import login
from tools.read_json import get_data
from tools.case_doc import case_doc
from parameterized import parameterized


class TestAddressManage(BaseCase):
    """收货地址管理"""

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.address = PageAddress(cls.driver)

    def setUp(self):
        super().setUp()
        login(self.driver)
        self.address.page_open_manage()

    def test_address_pagination(self):
        """地址管理：8 条地址分 2 页，第 2 页展示剩余 4 条"""
        self.assertEqual(self.address.page_get_addr_count(), 4)
        self.assertIn("共 8 条", self.address.page_get_addr_pager_info())
        self.assertIn("1/2 页", self.address.page_get_addr_pager_info())

        self.address.page_click_addr_page(2)
        self.assertEqual(self.address.page_get_addr_count(), 4)

    def test_default_address_first(self):
        """地址管理：默认地址排名第一（排序）"""
        self.assertTrue(self.address.page_is_first_default())
        self.assertEqual(self.address.page_get_first_addr_name(), "张三")

    def test_default_address_count(self):
        """地址管理：初始有且仅有一个默认地址"""
        self.assertEqual(self.address.page_get_default_addr_count(), 1)

    @parameterized.expand(get_data("address_manage"), doc_func=case_doc)
    def test_add_address(self, name, phone, detail, success):
        """新增地址：合法保存成功（弹窗关闭+总数+1），非法停留在弹窗"""
        self.address.page_click_addr_add()
        self.assertTrue(self.address.page_modal_is_open())

        self.address.page_fill_modal_address(name, phone, detail)
        self.address.page_click_modal_button("保存")

        if success:
            self.assertFalse(self.address.page_modal_is_open())
            self.assertIn("共 9 条", self.address.page_get_addr_pager_info())
        else:
            self.assertTrue(self.address.page_modal_is_open())
            self.assertIn("共 8 条", self.address.page_get_addr_pager_info())

    def test_edit_address(self):
        """地址管理：编辑后收货人与地址内容更新"""
        self.address.page_edit_address(0, "张三丰", "13800138000", "北京市海淀区中关村大街1号")
        self.assertEqual(self.address.page_get_addr_name(0), "张三丰")
        self.assertIn("中关村", self.address.page_get_addr_detail(0))

    def test_delete_address(self):
        """地址管理：删除地址后总数减少"""
        self.address.page_delete_address(1)
        self.assertIn("共 7 条", self.address.page_get_addr_pager_info())

    def test_set_default_address(self):
        """地址管理：设为默认后原默认失效，且新默认置顶"""
        self.assertFalse(self.address.page_has_set_default_btn(0))
        self.assertTrue(self.address.page_has_set_default_btn(1))

        self.address.page_set_default_address(1)

        self.assertEqual(self.address.page_get_default_addr_count(), 1)
        self.assertTrue(self.address.page_is_first_default())
        self.assertEqual(self.address.page_get_first_addr_name(), "李四")


def tearDownModule():
    GetDriver().quit_driver()


if __name__ == "__main__":
    unittest.main(verbosity=2)