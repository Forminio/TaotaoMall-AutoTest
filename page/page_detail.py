from selenium.webdriver.common.by import By

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

    # ---------- 详情页长图 / 分区标签 / 猜你喜欢 ----------
    def page_long_img_count(self):
        """详情页广告长图由几张横图拼接而成，返回拼接图片张数"""
        return len(self.base_finds(page.detail_long_img))

    def page_long_img_srcs(self):
        """详情页广告长图各拼接图的 src 地址列表"""
        return [el.get_attribute("src") for el in self.base_finds(page.detail_long_img)]

    def page_get_tab_count(self):
        return len(self.base_finds(page.detail_tabs))

    def page_get_tab_names(self):
        return [el.text for el in self.base_finds(page.detail_tabs)]

    def page_active_tab(self):
        for el in self.base_finds(page.detail_tabs):
            if "active" in el.get_attribute("class"):
                return el.text
        return ""

    def page_get_panel_text(self):
        return self.base_text(page.detail_panel_text)

    def page_click_tab(self, name):
        self.base_click((By.CSS_SELECTOR,
                         "#detailTabs .tab[data-tab='" + name + "']"))

    def page_get_reco_count(self):
        return len(self.base_finds(page.reco_cards))

    def page_get_reco_names(self):
        return [el.text for el in self.base_finds(page.reco_names)]

    def page_get_reco_head(self):
        return self.base_text(page.reco_head)

    def page_click_reco(self, index=0):
        self.base_finds(page.reco_cards)[index].click()