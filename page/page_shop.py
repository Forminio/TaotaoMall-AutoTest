from selenium.webdriver.common.by import By

from base.base import Base
import page


class PageShop(Base):
    """店铺 / 商家详情页 / 卖家中心"""

    def page_click_nav_seller_center(self):
        self.base_click(page.nav_seller_center)

    def page_click_shop_link(self):
        """从商品详情页点击「进入店铺」"""
        self.base_click(page.detail_shop_link)

    def page_click_shop_back(self):
        self.base_click(page.shop_back_btn)

    def page_is_on_shop(self):
        return self.base_find(page.shop_box).is_displayed()

    def page_get_shop_name(self):
        return self.base_text(page.shop_name)

    def page_get_shop_stats(self):
        return self.base_text(page.shop_stats)

    def page_get_shop_desc(self):
        return self.base_text(page.shop_desc)

    def page_get_shop_product_title(self):
        return self.base_text(page.shop_product_title)

    def page_get_shop_product_count(self):
        return len(self.base_finds(page.shop_product_cards))

    def page_get_detail_shop_name(self):
        return self.base_text(page.detail_shop_name)

    def page_get_detail_shop_stats(self):
        return self.base_text(page.detail_shop_stats)

    # ---------- 卖家中心 ----------
    def page_is_on_seller(self):
        return self.base_find(page.seller_box).is_displayed()

    def page_click_seller_back(self):
        self.base_click(page.seller_back_btn)

    def page_get_seller_title(self):
        return self.base_text(page.seller_title)

    def page_get_seller_count(self):
        return len(self.base_finds(page.seller_shop_cards))

    def page_get_seller_names(self):
        return [el.text for el in self.base_finds(page.seller_shop_names)]

    def page_click_seller_shop(self, index=0):
        """点击第 index 个商家卡片进入店铺页"""
        self.base_finds(page.seller_shop_cards)[index].click()

    # ---------- 卖家中心：排行榜 / 类型 / 分页 ----------
    def page_get_rank_count(self):
        return len(self.base_finds(page.seller_rank_items))

    def page_get_rank_names(self):
        return [el.text for el in self.base_finds(page.seller_rank_names)]

    def page_get_first_rank_sales(self):
        return self.base_finds(page.seller_rank_sales)[0].text

    def page_click_rank(self, index=0):
        self.base_finds(page.seller_rank_items)[index].click()

    def page_get_type_names(self):
        return [el.text for el in self.base_finds(page.seller_tabs)]

    def page_click_type(self, name):
        for tab in self.base_finds(page.seller_tabs):
            if tab.text.strip() == name:
                tab.click()
                return
        raise AssertionError(f"卖家中心未找到分类: {name}")

    def page_get_seller_pager_info(self):
        return self.base_text((By.CSS_SELECTOR, "#sellerPager .page-info"))

    def page_click_seller_page(self, num):
        self.base_click((By.CSS_SELECTOR, f"#sellerPager .page-num[data-p='{num}']"))

    def page_seller_pager_visible(self):
        return self.base_find((By.CSS_SELECTOR, "#sellerPager")).is_displayed()