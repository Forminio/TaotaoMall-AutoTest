from selenium.webdriver.support.select import Select

from base.base import Base
import page


class PageCoupon(Base):
    """结算页 · 优惠券"""

    def page_select_coupon(self, value):
        """按 option 的 value 选择优惠券"""
        Select(self.base_find(page.coupon_select)).select_by_value(value)

    def page_get_order_summary(self):
        return self.base_text(page.order_summary)