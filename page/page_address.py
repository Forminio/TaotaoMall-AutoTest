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