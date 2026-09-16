from selenium.webdriver.common.by import By

from base.base import Base
import page


class PageAddress(Base):
    """收货地址 / 结算页"""

    def page_input_receiver(self, value):
        self.base_input(page.receiver, value)

    def page_input_phone(self, value):
        self.base_input(page.phone, value)

    def page_input_address(self, value):
        self.base_input(page.address, value)

    def page_input_remark(self, value):
        self.base_input(page.remark, value)

    def page_click_submit(self):
        self.base_click(page.submit_order_btn)

    def page_is_on_checkout(self):
        return self.base_is_exist(page.checkout_box)

    def page_fill_address(self, receiver, phone, address, remark=""):
        self.page_input_receiver(receiver)
        self.page_input_phone(phone)
        self.page_input_address(address)
        if remark:
            self.page_input_remark(remark)

    # ---------- 地址管理 ----------
    def page_is_on_manage(self):
        return self.base_find(page.address_manage_box).is_displayed()

    def page_open_manage(self):
        """进入地址管理页：个人中心 → 管理收货地址"""
        self.base_click(page.nav_user_center)
        self.base_click(page.uc_manager_address)

    def page_click_addr_add(self):
        self.base_click(page.addr_add_btn)

    def page_get_addr_count(self):
        return len(self.base_finds(page.addr_items))

    def page_get_default_addr_count(self):
        return len(self.base_finds(page.addr_default_items))

    def page_get_first_addr_name(self):
        names = self.base_finds(page.addr_names)
        return names[0].text

    def page_get_addr_name(self, index=0):
        return self.base_finds(page.addr_names)[index].text

    def page_get_addr_detail(self, index=0):
        return self.base_finds(page.addr_details)[index].text

    def page_is_first_default(self):
        """首个地址是否为默认地址"""
        items = self.base_finds(page.addr_items)
        return "default" in (items[0].get_attribute("class") or "").split()

    # ---------- modal 弹窗 ----------
    def page_modal_is_open(self):
        return self.base_find(page.modal_overlay).is_displayed()

    def page_click_modal_button(self, text):
        """按按钮文本点击弹窗底部按钮（如「保存」「删除」「取消」）"""
        for btn in self.base_finds(page.modal_buttons):
            if btn.text.strip() == text:
                btn.click()
                return
        raise AssertionError(f"弹窗中未找到按钮: {text}")

    def page_fill_modal_address(self, name, phone, detail):
        self.base_input(page.m_addr_name, name)
        self.base_input(page.m_addr_phone, phone)
        self.base_input(page.m_addr_detail, detail)

    def page_edit_address(self, index, name, phone, detail):
        """编辑第 index 个地址"""
        items = self.base_finds(page.addr_items)
        items[index].find_elements(By.CSS_SELECTOR, "button[data-act='edit']")[0].click()
        self.page_fill_modal_address(name, phone, detail)
        self.page_click_modal_button("保存")

    def page_delete_address(self, index):
        """删除第 index 个地址（弹窗二次确认）"""
        items = self.base_finds(page.addr_items)
        items[index].find_elements(By.CSS_SELECTOR, "button[data-act='del']")[0].click()
        self.page_click_modal_button("删除")

    def page_set_default_address(self, index):
        """将第 index 个地址设为默认"""
        items = self.base_finds(page.addr_items)
        items[index].find_elements(By.CSS_SELECTOR, "button[data-act='default']")[0].click()

    def page_has_set_default_btn(self, index):
        items = self.base_finds(page.addr_items)
        return len(items[index].find_elements(By.CSS_SELECTOR, "button[data-act='default']")) > 0