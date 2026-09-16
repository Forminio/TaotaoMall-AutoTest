from selenium.webdriver.common.by import By

from base.base import Base
import page


class PageMessages(Base):
    """消息中心：系统消息 / 客服消息"""

    def page_click_nav_messages(self):
        self.base_click(page.nav_messages)

    def page_click_nav_customer_service(self):
        self.base_click(page.nav_customer_service)

    def page_is_on_messages(self):
        return self.base_find(page.messages_box).is_displayed()

    def page_get_badge(self):
        return self.base_text(page.msg_badge)

    def page_badge_visible(self):
        return self.base_find(page.msg_badge).is_displayed()

    def page_click_tab_system(self):
        self.base_click(page.msg_tab_system)

    def page_click_tab_service(self):
        self.base_click(page.msg_tab_service)

    # ---------- 系统消息 ----------
    def page_get_sys_msg_count(self):
        return len(self.base_finds(page.sys_msg_items))

    def page_get_unread_count(self):
        """未读数可能为 0，不能走 base_finds（其等待至少出现一个元素），直接同步统计"""
        return len(self.driver.find_elements(*page.sys_msg_unread))

    def page_get_sys_msg_title(self, index=0):
        return self.base_finds(page.sys_msg_titles)[index].text

    def page_click_sys_message(self, index=0):
        self.base_finds(page.sys_msg_items)[index].click()

    def page_mark_all_read(self):
        self.base_click(page.mark_all_read_btn)

    # ---------- 客服消息 ----------
    def page_get_cs_msg_count(self):
        return len(self.base_finds(page.cs_msgs))

    def page_get_last_cs_reply(self):
        """最后一条客服消息气泡文本"""
        return self.base_finds(page.cs_bubbles)[-1].text

    def page_cs_send(self, text):
        self.base_input(page.cs_input, text)
        self.base_click(page.cs_send_btn)

    # ---------- 消息分页 ----------
    def page_get_msg_pager_info(self):
        return self.base_text((By.CSS_SELECTOR, "#msgPager .page-info"))

    def page_click_msg_page(self, num):
        self.base_click((By.CSS_SELECTOR, f"#msgPager .page-num[data-p='{num}']"))

    def page_msg_pager_visible(self):
        return self.base_find((By.CSS_SELECTOR, "#msgPager")).is_displayed()

    def page_click_back(self):
        self.base_click(page.messages_back_btn)