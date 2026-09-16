import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from base.get_driver import GetDriver
from base.base_case import BaseCase
from page.page_messages import PageMessages
from page.page_modal import PageModal
from page.page_user import PageUser
from common.flows import login
from tools.read_json import get_data
from tools.case_doc import case_doc
from parameterized import parameterized


class TestMessages(BaseCase):
    """消息中心"""

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.messages = PageMessages(cls.driver)
        cls.modal = PageModal(cls.driver)
        cls.user = PageUser(cls.driver)

    def setUp(self):
        super().setUp()
        login(self.driver)

    def test_messages_nav_open(self):
        """消息中心：点击顶栏「消息」进入，系统消息分 3 页每页 5 条"""
        self.messages.page_click_nav_messages()
        self.assertTrue(self.messages.page_is_on_messages())
        self.assertEqual(self.messages.page_get_sys_msg_count(), 5)
        self.assertTrue(self.messages.page_msg_pager_visible())
        self.assertIn("共 12 条", self.messages.page_get_msg_pager_info())
        self.assertIn("1/3 页", self.messages.page_get_msg_pager_info())

    def test_messages_sys_pagination(self):
        """消息中心：系统消息切到第 3 页展示剩余 2 条"""
        self.messages.page_click_nav_messages()
        self.messages.page_click_msg_page(3)
        self.assertEqual(self.messages.page_get_sys_msg_count(), 2)
        self.assertIn("3/3 页", self.messages.page_get_msg_pager_info())

    def test_messages_unread_badge(self):
        """消息中心：初始未读徽章为 12，全部已读后徽章隐藏"""
        self.assertTrue(self.messages.page_badge_visible())
        self.assertEqual(self.messages.page_get_badge(), "12")

        self.messages.page_click_nav_messages()
        self.messages.page_mark_all_read()

        self.assertFalse(self.messages.page_badge_visible())

    def test_messages_read_detail_modal(self):
        """消息中心：点击未读消息弹出正文弹窗且未读数减一"""
        self.messages.page_click_nav_messages()
        first_title = self.messages.page_get_sys_msg_title(0)

        self.messages.page_click_sys_message(0)

        self.assertTrue(self.modal.page_modal_is_open())
        self.assertEqual(self.modal.page_get_modal_title(), first_title)
        self.assertTrue(self.modal.page_get_modal_body())
        self.modal.page_click_modal_button("关闭")
        self.assertEqual(self.messages.page_get_badge(), "11")

    def test_messages_tab_switch(self):
        """消息中心：切换到客服消息展示聊天窗口"""
        self.messages.page_click_nav_messages()
        self.messages.page_click_tab_service()
        self.assertGreaterEqual(self.messages.page_get_cs_msg_count(), 3)

    @parameterized.expand(get_data("cs_reply"), doc_func=case_doc)
    def test_messages_cs_reply(self, question, expect_reply):
        """客服消息：提问后自动回复匹配关键词，记录追加两条"""
        self.messages.page_click_nav_messages()
        self.messages.page_click_tab_service()
        before = self.messages.page_get_cs_msg_count()

        self.messages.page_cs_send(question)

        self.assertEqual(self.messages.page_get_cs_msg_count(), before + 2)
        self.assertIn(expect_reply, self.messages.page_get_last_cs_reply())

    def test_messages_cs_empty_input(self):
        """客服消息：空内容发送不产生新记录"""
        self.messages.page_click_nav_messages()
        self.messages.page_click_tab_service()
        before = self.messages.page_get_cs_msg_count()

        self.messages.page_cs_send("")

        self.assertEqual(self.messages.page_get_cs_msg_count(), before)


class TestMessagesReverse(BaseCase):
    """消息中心反向用例"""

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.messages = PageMessages(cls.driver)
        cls.user = PageUser(cls.driver)

    def setUp(self):
        super().setUp()

    def test_messages_require_login(self):
        """消息中心：未登录点击「消息」被拦截"""
        self.messages.page_click_nav_messages()
        self.assertFalse(self.messages.page_is_on_messages())
        self.assertEqual(self.user.page_get_user_info(), "未登录")

    def test_customer_service_require_login(self):
        """客服消息：未登录点击「联系客服」被拦截"""
        self.messages.page_click_nav_customer_service()
        self.assertFalse(self.messages.page_is_on_messages())
        self.assertEqual(self.user.page_get_user_info(), "未登录")


def tearDownModule():
    GetDriver().quit_driver()


if __name__ == "__main__":
    unittest.main(verbosity=2)