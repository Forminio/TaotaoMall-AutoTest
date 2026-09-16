from base.base import Base
import page


class PageBanner(Base):
    """首页广告轮播"""

    def page_banner_visible(self):
        return self.base_find(page.banner_box).is_displayed()

    def page_get_banner_count(self):
        return len(self.base_finds(page.banner_items))

    def page_get_active_index(self):
        return self.base_find(page.banner_active).get_attribute("data-index")

    def page_click_dot(self, index):
        self.base_finds(page.banner_dots)[index].click()

    def page_get_dot_count(self):
        return len(self.base_finds(page.banner_dots))

    def page_close_banner(self):
        self.base_click(page.banner_close_btn)