from base.base import Base
import page


class PageUser(Base):
    """个人中心 / 我的订单"""

    def page_click_nav_orders(self):
        self.base_click(page.nav_orders)

    def page_is_on_orders(self):
        return self.base_is_exist(page.orders_box)

    def page_get_order_count(self):
        return len(self.base_finds(page.order_items))

    def page_is_orders_empty(self):
        return self.base_is_exist(page.orders_empty)

    def page_get_user_info(self):
        return self.base_text(page.user_info)