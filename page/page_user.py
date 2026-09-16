from selenium.webdriver.common.by import By

from base.base import Base
import page


class PageUser(Base):
    """个人中心 / 我的订单"""

    def page_click_nav_orders(self):
        self.base_click(page.nav_orders)

    def page_is_on_orders(self):
        return self.base_find(page.orders_box).is_displayed()

    def page_get_order_count(self):
        return len(self.base_finds(page.order_items))

    # ---------- 订单分页 ----------
    def page_get_orders_pager_info(self):
        return self.base_text((By.CSS_SELECTOR, "#ordersPager .page-info"))

    def page_get_orders_page_count(self):
        return len(self.base_finds((By.CSS_SELECTOR, "#ordersPager .page-num")))

    def page_click_orders_page(self, num):
        self.base_click((By.CSS_SELECTOR, f"#ordersPager .page-num[data-p='{num}']"))

    def page_is_orders_empty(self):
        return self.base_is_exist(page.orders_empty)

    def page_get_user_info(self):
        return self.base_text(page.user_info)

    # ---------- 个人中心 ----------
    def page_click_nav_user_center(self):
        self.base_click(page.nav_user_center)

    def page_is_on_user_center(self):
        return self.base_find(page.user_center_box).is_displayed()

    def page_get_uc_name(self):
        return self.base_text(page.uc_name)

    def page_get_uc_phone(self):
        return self.base_text(page.uc_phone)

    def page_get_uc_order_count(self):
        return self.base_text(page.uc_order_count)

    def page_get_uc_addr_count(self):
        return self.base_text(page.uc_addr_count)

    def page_click_uc_nav_orders(self):
        self.base_click(page.uc_nav_orders)

    def page_click_uc_nav_address(self):
        self.base_click(page.uc_nav_address)

    def page_click_uc_manager_address(self):
        self.base_click(page.uc_manager_address)

    def page_click_uc_my_orders(self):
        self.base_click(page.uc_my_orders)

    def page_click_uc_logout(self):
        self.base_click(page.uc_logout)