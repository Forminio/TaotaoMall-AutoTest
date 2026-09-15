"""高层业务流程封装，供测试用例复用，消除重复代码。"""

from page.page_login import PageLogin
from page.page_product import PageProduct
from page.page_cart import PageCart

DEFAULT_USER = "admin"
DEFAULT_PASSWORD = "123456"
DEFAULT_CAPTCHA = "8888"


def login(driver, username=DEFAULT_USER, password=DEFAULT_PASSWORD, captcha=DEFAULT_CAPTCHA):
    """点击登录入口并完成登录，返回登录页对象。"""
    page = PageLogin(driver)
    page.page_click_login_link()
    page.page_login(username, password, captcha)
    return page


def checkout(driver, index=0):
    """商品列表加购第 index 个商品 → 进入购物车 → 跳转结算页。"""
    PageProduct(driver).page_add_cart(index)
    PageCart(driver).page_click_nav_cart()
    PageCart(driver).page_click_checkout()