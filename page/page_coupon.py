from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from base.base import Base
import page


class PageCoupon(Base):
    """结算页 · 优惠券 / 我的优惠券"""

    def page_select_coupon(self, value):
        """按 option 的 value 选择优惠券"""
        Select(self.base_find(page.coupon_select)).select_by_value(value)

    def page_get_order_summary(self):
        return self.base_text(page.order_summary)

    # ---------- 我的优惠券 ----------
    def page_click_nav_coupons(self):
        self.base_click(page.nav_coupons)

    def page_click_uc_my_coupons(self):
        self.base_click(page.uc_my_coupons)

    def page_is_on_coupons(self):
        return self.base_find(page.coupons_box).is_displayed()

    def page_get_coupon_count(self):
        """当前页展示的券数（分页后为当页数量）"""
        return len(self.base_finds(page.coupon_cards))

    def page_get_coupon_statuses(self):
        return [el.text for el in self.base_finds(page.coupon_statuses)]

    def page_get_coupon_titles(self):
        return [el.text for el in self.base_finds(page.coupon_titles)]

    def page_get_pager_info(self):
        return self.base_text((By.CSS_SELECTOR, "#couponPager .page-info"))

    def page_click_pager_page(self, num):
        self.base_click((By.CSS_SELECTOR, f"#couponPager .page-num[data-p='{num}']"))

    def page_click_use(self, index=0):
        self.base_finds(page.coupon_use_btns)[index].click()