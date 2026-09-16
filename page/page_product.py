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

    # ---------- 分页 ----------
    def page_get_page_info(self):
        return self.base_text(page.pagination_info)

    def page_get_active_page(self):
        return self.base_text(page.pagination_active_page)

    def page_get_page_num_count(self):
        return len(self.base_finds(page.pagination_page_nums))

    def page_click_page(self, num):
        """点击指定页码（页码文本）"""
        self.base_click((By.CSS_SELECTOR, f"#pagination .page-num[data-page='{num}']"))

    def page_click_next_page(self):
        """点击「下一页」按钮（按文本定位）"""
        for btn in self.base_finds((By.CSS_SELECTOR, "#pagination button")):
            if btn.text.strip() == "下一页":
                btn.click()
                return

    def page_click_prev_page(self):
        """点击「上一页」按钮（按文本定位）"""
        for btn in self.base_finds((By.CSS_SELECTOR, "#pagination button")):
            if btn.text.strip() == "上一页":
                btn.click()
                return

    # ---------- 搜索店铺 ----------
    def page_search_shops_visible(self):
        return self.base_find(page.search_shops).is_displayed()

    def page_get_search_shop_count(self):
        return len(self.base_finds(page.search_shop_cards))

    def page_get_search_shop_names(self):
        return [el.find_element(By.CSS_SELECTOR, ".sc-name").text
                for el in self.base_finds(page.search_shop_cards)]

    def page_click_search_shop(self, index=0):
        self.base_finds(page.search_shop_cards)[index].click()