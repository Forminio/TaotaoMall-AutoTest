from selenium.webdriver.common.by import By

from base.base import Base
import page
from tools.price import parse_price


class PageProduct(Base):
    """商品列表页"""

    def page_get_product_title(self):
        return self.base_text(page.product_title)

    def page_get_product_count(self):
        """demo 为同步渲染，点击搜索/分类后 DOM 已随之更新，直接统计即可"""
        return len(self.driver.find_elements(*page.product_cards))

    def page_get_product_name(self, index=0):
        """读取第 index 个商品的名称"""
        names = self.base_finds(page.product_names)
        return names[index].text

    def page_get_product_price(self, index=0):
        """读取第 index 个商品的展示价格，返回整数"""
        prices = self.base_finds(page.product_prices)
        return parse_price(prices[index].text)

    def page_click_category(self, cat):
        self.base_click((By.CSS_SELECTOR, f".cat-link[data-cat='{cat}']"))

    def page_input_search(self, keyword):
        self.base_input(page.search_input, keyword)

    def page_click_search(self):
        self.base_click(page.search_btn)

    def page_click_product(self, index=0):
        cards = self.base_finds(page.product_cards)
        cards[index].click()

    def page_add_cart(self, index=0):
        btns = self.base_finds(page.add_cart_btns)
        btns[index].click()

    def page_search(self, keyword):
        self.page_input_search(keyword)
        self.page_click_search()