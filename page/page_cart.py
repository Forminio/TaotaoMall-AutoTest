from selenium.webdriver.common.by import By

from base.base import Base
import page


class PageCart(Base):
    """购物车页"""

    def page_click_nav_cart(self):
        self.base_click(page.nav_cart)

    def page_get_cart_total(self):
        return self.base_text(page.cart_total)

    def page_click_qty_plus(self, index=0):
        btns = self.base_finds(page.qty_plus)
        btns[index].click()

    def page_click_qty_minus(self, index=0):
        btns = self.base_finds(page.qty_minus)
        btns[index].click()

    def page_get_qty(self, index=0):
        vals = self.base_finds(page.qty_value)
        return vals[index].get_attribute("value")

    def page_click_del(self, index=0):
        dels = self.base_finds(page.cart_del)
        dels[index].click()

    def page_click_clear(self):
        self.base_click(page.clear_cart_btn)
        alert = self.base_get_alert()
        alert.accept()

    def page_click_checkout(self):
        self.base_click(page.checkout_btn)

    def page_is_cart_empty(self):
        return self.base_is_exist(page.cart_empty)

    # ---------- 购物车分页 ----------
    def page_get_row_count(self):
        return len(self.base_finds(page.cart_rows))

    def page_get_pager_info(self):
        return self.base_text((By.CSS_SELECTOR, "#cartPager .page-info"))

    def page_click_pager_page(self, num):
        self.base_click((By.CSS_SELECTOR, f"#cartPager .page-num[data-p='{num}']"))