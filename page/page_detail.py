from base.base import Base
import page


class PageDetail(Base):
    """商品详情页"""

    def page_get_detail_name(self):
        return self.base_text(page.detail_name)

    def page_get_detail_price(self):
        return self.base_text(page.detail_price)

    def page_get_detail_stock(self):
        return self.base_text(page.detail_stock)

    def page_get_detail_qty(self):
        return self.base_value(page.detail_qty)

    def page_click_plus(self):
        self.base_click(page.detail_plus)

    def page_click_minus(self):
        self.base_click(page.detail_minus)

    def page_click_add_cart(self):
        self.base_click(page.detail_add_cart)

    def page_click_buy_now(self):
        self.base_click(page.detail_buy_now)

    def page_set_qty(self, qty):
        el = self.base_find(page.detail_qty)
        el.clear()
        el.send_keys(str(qty))