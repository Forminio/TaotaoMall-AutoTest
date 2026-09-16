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
nav_user_center = (By.ID, "navUserCenter")
nav_seller_center = (By.ID, "navSellerCenter")
nav_messages = (By.ID, "navMessages")
nav_customer_service = (By.ID, "navCustomerService")
nav_coupons = (By.ID, "navCoupons")
nav_address = (By.ID, "navAddress")

# ==================== 广告轮播 ====================
banner_box = (By.ID, "bannerBox")
banner_items = (By.CSS_SELECTOR, "#bannerView .banner-item")
banner_active = (By.CSS_SELECTOR, "#bannerView .banner-item.active")
banner_dots = (By.CSS_SELECTOR, "#bannerDots .banner-dot")
banner_close_btn = (By.ID, "bannerCloseBtn")

# ==================== 我的优惠券 ====================
coupons_box = (By.ID, "couponsBox")
coupon_cards = (By.CSS_SELECTOR, "#couponList .coupon-card")
coupon_use_btns = (By.CSS_SELECTOR, "#couponList .cc-use")
coupon_statuses = (By.CSS_SELECTOR, "#couponList .cc-status")
coupon_titles = (By.CSS_SELECTOR, "#couponList .cc-title")
coupons_back_btn = (By.ID, "couponsBackBtn")
uc_my_coupons = (By.ID, "ucMyCoupons")

# ==================== 搜索店铺 ====================
search_shops = (By.ID, "searchShops")
search_shop_cards = (By.CSS_SELECTOR, "#searchShops .shop-card")

# ==================== 卖家中心增强 ====================
seller_tabs = (By.CSS_SELECTOR, "#sellerTabs .seller-tab")
seller_rank_items = (By.CSS_SELECTOR, "#sellerRank .rank-item")
seller_rank_names = (By.CSS_SELECTOR, "#sellerRank .rank-name")
seller_rank_sales = (By.CSS_SELECTOR, "#sellerRank .rank-sales")

# ==================== 卖家中心 ====================
seller_box = (By.ID, "sellerBox")
seller_title = (By.ID, "sellerTitle")
shop_list = (By.ID, "shopList")
seller_shop_cards = (By.CSS_SELECTOR, "#shopList .shop-card")
seller_shop_names = (By.CSS_SELECTOR, "#shopList .sc-name")
seller_back_btn = (By.ID, "sellerBackBtn")

# ==================== 消息中心 ====================
messages_box = (By.ID, "messagesBox")
msg_badge = (By.ID, "msgBadge")
msg_tab_system = (By.ID, "msgTabSystem")
msg_tab_service = (By.ID, "msgTabService")
msg_tab_content = (By.ID, "msgTabContent")
sys_msg_items = (By.CSS_SELECTOR, "#msgTabContent .sys-msg-item")
sys_msg_unread = (By.CSS_SELECTOR, "#msgTabContent .sys-msg-item.unread")
sys_msg_titles = (By.CSS_SELECTOR, "#msgTabContent .sys-msg-title")
mark_all_read_btn = (By.ID, "markAllReadBtn")
cs_msgs = (By.CSS_SELECTOR, "#msgTabContent .cs-msg")
cs_bubbles = (By.CSS_SELECTOR, "#msgTabContent .cs-msg .bubble")
cs_input = (By.ID, "csInput")
cs_send_btn = (By.ID, "csSendBtn")
messages_back_btn = (By.ID, "messagesBackBtn")

# ==================== 页脚 / 协议 ====================
foot_links = (By.CSS_SELECTOR, ".foot-link")
login_agreement_link = (By.ID, "loginAgreementLink")
login_privacy_link = (By.ID, "loginPrivacyLink")
reg_agreement_link = (By.ID, "regAgreementLink")
reg_privacy_link = (By.ID, "regPrivacyLink")

# ==================== toast 提示 ====================
toast = (By.CSS_SELECTOR, ".toast")

# ==================== 商品分页 ====================
pagination = (By.ID, "pagination")
pagination_info = (By.CSS_SELECTOR, "#pagination .page-info")
pagination_page_nums = (By.CSS_SELECTOR, "#pagination .page-num")
pagination_active_page = (By.CSS_SELECTOR, "#pagination .page-num.active")

# ==================== 详情页店铺信息 ====================
detail_shop_logo = (By.ID, "detailShopLogo")
detail_shop_name = (By.ID, "detailShopName")
detail_shop_stats = (By.ID, "detailShopStats")
detail_shop_link = (By.ID, "detailShopLink")
# 详情页长图 / 分区标签 / 内容面板 / 猜你喜欢
detail_long_img = (By.CSS_SELECTOR, "#detailLong img")
detail_tabs = (By.CSS_SELECTOR, "#detailTabs .tab")
detail_panel = (By.ID, "detailPanel")
detail_panel_text = (By.CSS_SELECTOR, "#detailPanel")
detail_tab_desc = (By.CSS_SELECTOR, "#detailTabs .tab[data-tab='desc']")
detail_tab_usage = (By.CSS_SELECTOR, "#detailTabs .tab[data-tab='usage']")
detail_tab_disclaimer = (By.CSS_SELECTOR, "#detailTabs .tab[data-tab='disclaimer']")
detail_tab_recommend = (By.CSS_SELECTOR, "#detailTabs .tab[data-tab='recommend']")
reco_cards = (By.CSS_SELECTOR, "#detailPanel .reco-card")
reco_names = (By.CSS_SELECTOR, "#detailPanel .rc-name")
reco_prices = (By.CSS_SELECTOR, "#detailPanel .rc-price")
reco_head = (By.CSS_SELECTOR, "#detailPanel .reco-head")

# ==================== 店铺页 ====================
shop_box = (By.ID, "shopBox")
shop_back_btn = (By.ID, "shopBackBtn")
shop_logo = (By.ID, "shopLogo")
shop_name = (By.ID, "shopName")
shop_stats = (By.ID, "shopStats")
shop_desc = (By.ID, "shopDesc")
shop_product_title = (By.ID, "shopProductTitle")
shop_products = (By.ID, "shopProducts")
shop_product_cards = (By.CSS_SELECTOR, "#shopProducts .product-card")

# ==================== 个人中心 ====================
user_center_box = (By.ID, "userCenterBox")
uc_name = (By.ID, "ucName")
uc_phone = (By.ID, "ucPhone")
uc_order_count = (By.ID, "ucOrderCount")
uc_addr_count = (By.ID, "ucAddrCount")
uc_nav_orders = (By.ID, "ucNavOrders")
uc_nav_address = (By.ID, "ucNavAddress")
uc_manager_address = (By.ID, "ucManagerAddress")
uc_my_orders = (By.ID, "ucMyOrders")
uc_logout = (By.ID, "ucLogout")

# ==================== 地址管理 ====================
address_manage_box = (By.ID, "addressManageBox")
addr_list = (By.ID, "addrList")
addr_add_btn = (By.ID, "addrAddBtn")
addr_back_btn = (By.ID, "addrBackBtn")
addr_items = (By.CSS_SELECTOR, "#addrList .addr-item")
addr_default_items = (By.CSS_SELECTOR, "#addrList .addr-item.default")
addr_names = (By.CSS_SELECTOR, "#addrList .addr-name-text")
addr_phones = (By.CSS_SELECTOR, "#addrList .addr-phone")
addr_details = (By.CSS_SELECTOR, "#addrList .addr-detail")

# ==================== modal 弹窗 ====================
modal_overlay = (By.ID, "modalOverlay")
modal_title = (By.ID, "modalTitle")
modal_body = (By.ID, "modalBody")
modal_footer = (By.ID, "modalFooter")
modal_buttons = (By.CSS_SELECTOR, "#modalFooter button")
m_addr_name = (By.ID, "mAddrName")
m_addr_phone = (By.ID, "mAddrPhone")
m_addr_detail = (By.ID, "mAddrDetail")