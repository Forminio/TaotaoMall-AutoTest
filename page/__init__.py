from selenium.webdriver.common.by import By

# ==================== 登录页 ====================
login_link = (By.PARTIAL_LINK_TEXT, "登录")
logout_link = (By.PARTIAL_LINK_TEXT, "退出")
login_username = (By.ID, "username")
login_password = (By.ID, "password")
login_captcha = (By.ID, "captcha")
login_captcha_box = (By.ID, "captchaBox")
login_agree = (By.ID, "agree")
login_btn = (By.ID, "loginBtn")
login_msg = (By.ID, "loginMsg")
user_info = (By.ID, "userInfo")
goto_register_link = (By.ID, "gotoRegisterLink")

# ==================== 注册页 ====================
register_box = (By.ID, "registerBox")
reg_username = (By.ID, "regUsername")
reg_password = (By.ID, "regPassword")
reg_confirm = (By.ID, "regConfirm")
reg_phone = (By.ID, "regPhone")
reg_agree = (By.ID, "regAgree")
reg_btn = (By.ID, "regBtn")
reg_msg = (By.ID, "regMsg")
back_login_link = (By.ID, "backLoginLink")

# ==================== 商品列表 ====================
product_box = (By.ID, "productBox")
product_title = (By.ID, "productTitle")
product_cards = (By.CSS_SELECTOR, ".product-card")
product_names = (By.CSS_SELECTOR, ".product-name")
product_prices = (By.CSS_SELECTOR, ".product-price")
add_cart_btns = (By.CSS_SELECTOR, ".btn-add")

# ==================== 分类导航 ====================
cat_links = (By.CSS_SELECTOR, ".cat-link")

# ==================== 搜索 ====================
search_input = (By.ID, "searchInput")
search_btn = (By.ID, "searchBtn")

# ==================== 商品详情 ====================
detail_box = (By.ID, "detailBox")
detail_img = (By.ID, "detailImg")
detail_name = (By.ID, "detailName")
detail_price = (By.ID, "detailPrice")
detail_sales = (By.ID, "detailSales")
detail_cat = (By.ID, "detailCat")
detail_stock = (By.ID, "detailStock")
detail_qty = (By.ID, "detailQty")
detail_minus = (By.ID, "detailMinus")
detail_plus = (By.ID, "detailPlus")
detail_add_cart = (By.ID, "detailAddCart")
detail_buy_now = (By.ID, "detailBuyNow")

# ==================== 购物车 ====================
cart_box = (By.ID, "cartBox")
cart_list = (By.ID, "cartList")
cart_rows = (By.CSS_SELECTOR, "#cartList tr")
cart_total = (By.ID, "cartTotal")
cart_empty = (By.ID, "cartEmpty")
cart_footer = (By.ID, "cartFooter")
qty_plus = (By.CSS_SELECTOR, ".qty-plus")
qty_minus = (By.CSS_SELECTOR, ".qty-minus")
qty_value = (By.CSS_SELECTOR, ".qty-value")
cart_del = (By.CSS_SELECTOR, ".cart-del")
clear_cart_btn = (By.ID, "clearCartBtn")
checkout_btn = (By.ID, "checkoutBtn")
nav_cart = (By.ID, "navCart")

# ==================== 结算 / 地址 ====================
checkout_box = (By.ID, "checkoutBox")
receiver = (By.ID, "receiver")
phone = (By.ID, "phone")
address = (By.ID, "address")
remark = (By.ID, "remark")
order_summary = (By.ID, "orderSummary")
coupon_select = (By.ID, "couponSelect")
submit_order_btn = (By.ID, "submitOrderBtn")

# ==================== 下单成功 ====================
order_box = (By.ID, "orderBox")
order_no = (By.ID, "orderNo")
order_receiver = (By.ID, "orderReceiver")
order_phone = (By.ID, "orderPhone")
order_address = (By.ID, "orderAddress")
order_amount = (By.ID, "orderAmount")
order_time = (By.ID, "orderTime")
back_home_btn = (By.ID, "backHomeBtn")
view_orders_btn = (By.ID, "viewOrdersBtn")

# ==================== 我的订单 ====================
orders_box = (By.ID, "ordersBox")
orders_list = (By.ID, "ordersList")
orders_empty = (By.ID, "ordersEmpty")
order_items = (By.CSS_SELECTOR, ".order-item")

# ==================== 个人中心 ====================
nav_orders = (By.ID, "navOrders")
nav_login = (By.ID, "navLogin")
nav_register = (By.ID, "navRegister")
logo_btn = (By.ID, "logoBtn")

# ==================== 顶部导航 ====================
top_user_info = (By.ID, "userInfo")