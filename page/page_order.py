from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base import Base
import page


class PageOrder(Base):
    """订单结果页"""

    def page_get_order_no(self):
        return self.base_text(page.order_no)

    def page_get_order_receiver(self):
        return self.base_text(page.order_receiver)

    def page_get_order_amount(self):
        return self.base_text(page.order_amount)

    def page_get_order_time(self):
        return self.base_text(page.order_time)

    def page_click_back_home(self):
        self.base_click(page.back_home_btn)

    def page_click_view_orders(self):
        self.base_click(page.view_orders_btn)

    def page_get_order_count(self):
        return len(self.base_finds(page.order_items))

    def page_is_order_success(self):
        """下单成功页可见（而非仅元素存在）"""
        try:
            WebDriverWait(self.driver, 10, 0.5).until(
                EC.visibility_of_element_located(page.order_box)
            )
            return True
        except Exception:
            return False