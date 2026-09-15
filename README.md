<p align="center">
  <img src="https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/Selenium-4.x-43B02A?style=for-the-badge&logo=selenium&logoColor=white" alt="Selenium"/>
  <img src="https://img.shields.io/badge/unittest-驱动测试-FF5000?style=for-the-badge" alt="unittest"/>
  <img src="https://img.shields.io/badge/PageObject-设计模式-8A2BE2?style=for-the-badge" alt="PageObject"/>
  <img src="https://img.shields.io/badge/XTestRunner-报告内嵌截图-00CC88?style=for-the-badge" alt="XTestRunner"/>
</p>

<h1 align="center">🛒 淘淘商城 Web 自动化测试框架</h1>

<p align="center">
  一个 <b>从零搭起「可写进简历」</b> 的 UI 自动化测试工程 ——
  用 <b>PageObject + 数据驱动 + 单例浏览器 + 动态断言</b> 覆盖电商核心链路，<br/>
  并输出带 <b>失败截图</b> 的 HTML 测试报告。
</p>

<p align="center">
  <a href="#-为什么这个项目能加分"><b>✨ 核心亮点</b></a> ·
  <a href="#-架构设计">🏗️ 架构设计</a> ·
  <a href="#-技术栈">🧰 技术栈</a> ·
  <a href="#-快速开始">🚀 快速开始</a> ·
  <a href="#-设计亮点代码拆解">⚡ 设计亮点代码拆解</a> ·
  <a href="#-测试覆盖">🧪 测试覆盖</a>
</p>

---

## ✨ 为什么这个项目能加分

| 亮点 | 一句话解释 | 对应技术 |
| --- | --- | --- |
| 🧬 **浏览器单例** | 全套用例只启动 **一次 Chrome**，不再每类用例各起停一次 | 类级单例 + `setUpClass` |
| 🧩 **PageObject 分层** | 定位器 / 页面操作 / 测试用例三层解耦，改 UI 只动一处 | `page/` 目录 |
| 📊 **字典数据驱动** | JSON 用「命名参数」喂给用例，**彻底消灭位置错位** | `parameterized` + `param.explicit` |
| 🎯 **动态断言** | 期望金额 **运行时从页面读取**，不硬编码、不怕改价格 | `format_price / parse_price` |
| ♻️ **业务流程复用** | 登录 / 加购结算抽取成高阶命令，用例 3 行写完一条链路 | `common/flows.py` |
| 📸 **失败截图内嵌** | 失败用例自动 `base64` 截图写进 HTML 报告 | XTestRunner |
| 🧪 **用例隔离** | 每条用例重载页面重置 JS 内存状态，互不污染 | `BaseCase.setUp` |
| 🎭 **无头模式** | `HEADLESS=1` 一键切 CI/无人值守，不弹窗 | `Options` 环境变量 |

---

## 🏗️ 架构设计

```
                       ┌──────────────────────────────┐
                       │           main.py            │  统一入口：装配全部用例 → 跑 → 出报告 → 退出浏览器
                       └──────────────┬───────────────┘
                                      │ loadTestsFromTestCase
                       ┌──────────────▼───────────────┐
                       │   scripts/test_*.py          │  用例层（只写「做什么」）
                       │   @parameterized.expand(...)  │  ── 数据驱动 + 断言
                       └──────────────┬───────────────┘
                                      │ 调用高层业务流
                       ┌──────────────▼───────────────┐
                       │   common/flows.py            │  业务编排层（登录 / 加购结算）
                       └──────────────┬───────────────┘
                                      │ 组合 PageObject
                       ┌──────────────▼───────────────┐
                       │   page/page_*.py             │  页面对象层（每个页面一个 class）
                       │   page/__init__.py           │  ── 定位器统一管理
                       └──────────────┬───────────────┘
                                      │ 基础操作封装
                       ┌──────────────▼───────────────┐
                       │   base/base.py               │  显式等待 / 查找 / 输入 / JS 点击 / iframe…
                       │   base/base_case.py          │  统一基类：驱动获取 + 状态重置
                       │   base/get_driver.py         │  浏览器单例
                       └──────────────┬───────────────┘
                                      │ file:// 协议打开本地页面
                       ┌──────────────▼───────────────┐
                       │   demo/淘淘商城.html          │  被测页面（纯前端、无后端依赖）
                       └──────────────────────────────┘
```

**依赖方向是单向的**：用例 → 业务流 → 页面对象 → 基础封装 → 驱动。任何一层变更都不会向上污染。

---

## 🧰 技术栈

- **Python 3.9+** — 主语言
- **Selenium 4.x** — 浏览器自动化驱动
- **unittest** — 原生测试框架（不额外引入 pytest，保证零负担上手）
- **parameterized** — 数据驱动，让一条用例方法覆盖 N 组数据
- **XTestRunner** — HTML 报告，失败自动截图内嵌（base64）
- **被测对象** — 本地单文件 `demo/淘淘商城.html`，无需后端 / 服务器

---

## 📂 目录结构

```
TaotaoMall-AutoTest
├── main.py                    # 统一入口：加载全部用例 → 生成 HTML 报告 → 退出浏览器
├── base/
│   ├── get_driver.py          # 浏览器驱动单例（整个进程只开一次 Chrome）
│   ├── base.py                # 基础封装：显式等待 / 查找 / 输入 / JS 点击 / iframe
│   └── base_case.py           # 测试基类：驱动获取 + 用例状态重置（实现用例隔离）
├── common/
│   └── flows.py               # 高层业务流复用：login() / checkout()
├── page/
│   ├── __init__.py            # 所有元素定位器（统一管理，改 UI 只动这里）
│   └── page_*.py              # 各页面对象（login/product/detail/cart/coupon/address/order/user）
├── scripts/
│   └── test_*.py              # 测试用例（9 个模块，覆盖登录→下单全链路）
├── data/
│   └── *.json                 # 数据驱动测试数据（字典数组）
├── tools/
│   ├── read_json.py           # JSON 读取 + 命名参数封装
│   ├── price.py               # 金额格式化 / 解析（与前端逻辑保持一致）
│   └── case_doc.py            # 让报告「描述列」干净展示中文说明
├── reports/                   # 自动生成的 HTML 报告（已 gitignore）
├── requirements.txt
└── demo/淘淘商城.html          # 被测页面
```

---

## 🚀 快速开始

```bash
# 1. 安装依赖（需本机 Chrome 及配套 chromedriver）
pip install -r requirements.txt

# 2. 全量执行并生成报告
python main.py

# 3. 单独运行某个模块（脚本内置项目根路径注入，可直接跑）
python scripts/test_login.py

# 4. 无头模式（CI / 无人值守，不弹浏览器窗口）
#    Windows PowerShell
$env:HEADLESS="1"; python main.py
#    Linux / macOS
HEADLESS=1 python main.py
```

跑完会在 `reports/taotao_mall_report.html` 生成图表化 HTML 报告（ECharts 统计 + 失败截图）。

---

## ⚡ 设计亮点代码拆解

### 1. 浏览器单例 —— 一套用例只开一次 Chrome

关键不是「每次都能开」，而是「第二次起不再开」。用**类级属性**作为全局开关，进程内 `driver` 只构造一次：

```python
class GetDriver:
    driver = None          # 类级变量充当"单例委托人"

    @classmethod
    def get_driver(cls):
        if cls.driver is None:                 # 只有第一次豁免惰性构造
            options = Options()
            if os.getenv("HEADLESS") == "1":   # 无头模式开关
                options.add_argument("--headless=new")
            cls.driver = webdriver.Chrome(options=options)
            cls.driver.get(cls.get_url())
        return cls.driver                      # 之后都复用同一个实例

    @classmethod
    def quit_driver(cls):
        if cls.driver is not None:
            cls.driver.quit()
        cls.driver = None                      # 复位，允许下次重建
```

> 配合 `main.py` 在**全部用例执行完后**统一 `quit_driver()`，整轮测试 Chrome 起停各一次。

### 2. 字典数据驱动 —— 用「名字」而非「位置」喂参数

数组对齐容易 `password` 填进 `username`。改为 **JSON 字典数组 + `param.explicit(kwargs=...)`**，键名即形参名：

```python
# tools/read_json.py
def get_data(filename):
    data = read_json(DATA_DIR / f"{filename}.json")
    return [param.explicit(kwargs=item) for item in data]   # 键名 ↔ 形参名一一对应
```

```json
// data/login.json —— 键名与测试方法形参完全一致
[
  { "username": "admin",  "password": "123456", "captcha": "8888", "expect_msg": "",          "success": true  },
  { "username": "admin",  "password": "wrong",  "captcha": "8888", "expect_msg": "验证码错误", "success": false }
]
```

```python
@parameterized.expand(get_data("login"), doc_func=case_doc)   # doc_func 让报告描述列干净
def test_login(self, username, password, captcha, expect_msg, success):
    """登录功能：正确凭证登录成功，错误凭证给出对应提示"""
    ...
```

新增一条用例 = 往 JSON 加一行，**零代码改动**。

### 3. 动态金额断言 —— 期望值不是抄的，是算出来的

价格一旦写死，前端调价测试就「假绿」。这里**运行时读页面价格**，再用自己的 `price` 工具函数算期望，与前端 `formatPrice` 逻辑完全同源：

```python
# tools/price.py —— 与 demo 的 formatPrice 保持同一套千分位规则
def format_price(n):                 # 8999 -> '8,999'
    return f"{int(n):,}"

def parse_price(text):               # '¥8,999' -> 8999
    return int("".join(ch for ch in str(text) if ch.isdigit()))
```

```python
# scripts/test_order.py
def test_order(self, receiver, phone, address, remark, index):
    unit = self.product.page_get_product_price(index)     # 运行时读价，不写死
    checkout(self.driver, index)
    self.address.page_fill_address(receiver, phone, address, remark)
    self.address.page_click_submit()
    self.assertIn(format_price(unit), self.order.page_get_order_amount())   # 动态断言
```

优惠券更是把「门槛/减免」抽成一张**规则表**，测试端复算一遍应付金额：

```python
COUPON_RULES = {"n": (0, 0), "a": (5000, 500), "b": (3000, 200), "c": (1000, 50)}

def test_coupon(self, index, coupon):
    unit = self.product.page_get_product_price(index)
    threshold, discount = COUPON_RULES[coupon]
    payable = unit - discount if unit >= threshold else unit     # 复算折后价
    ...
    self.assertIn(format_price(payable), self.order.page_get_order_amount())
```

### 4. 业务流程复用 —— 高频链路一行提走

登录、加购结算在多条用例里反复出现，抽成高阶命令，避免 copy-paste：

```python
# common/flows.py
def login(driver, username="admin", password="123456", captcha="8888"):
    page = PageLogin(driver)
    page.page_click_login_link()
    page.page_login(username, password, captcha)
    return page

def checkout(driver, index=0):
    PageProduct(driver).page_add_cart(index)
    PageCart(driver).page_click_nav_cart()
    PageCart(driver).page_click_checkout()
```

用例层立刻变干净：`login(self.driver)` + `checkout(self.driver, i)` 两步进入结算页。

### 5. 用例隔离 —— 每条用例从「裸状态」出发

`BaseCase.setUp` 每跑一条用例前**重载页面**，把 demo 的 JS 内存状态（购物车 / 订单 / 登录态）整体清空，用例之间互不污染：

```python
class BaseCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = GetDriver().get_driver()      # 复用同一个浏览器

    def setUp(self):
        self.driver.get(GetDriver().get_url())      # 每次重载，重置 JS 状态
```

### 6. 显式等待 + JS 兜底点击 —— 抗抖动的健壮性封装

放弃脆弱的 `time.sleep`，统一走 Selenium 显式等待；普通 `click` 点不动时用 JS 强制点击兜底：

```python
class Base:
    def base_find(self, loc, timeout=10, poll=0.5):
        return WebDriverWait(self.driver, timeout, poll_frequency=poll).until(
            lambda d: d.find_element(*loc)
        )

    def base_js_click(self, loc):                   # 元素被遮挡时的兜底方案
        el = self.base_find(loc)
        self.driver.execute_script("arguments[0].click();", el)
```

### 7. 失败截图内嵌报告 —— 排查零成本

XTestRunner 检测到用例存在 `WebDriver` 且失败时，**自动截图转 base64 内嵌 HTML**，无需在用例里写任何截图代码：

```python
# main.py
runner = HTMLTestRunner(
    stream=fp,
    title="淘淘商城 自动化测试报告",
    language="zh-CN",
    tester="forminio",
)
runner.run(suite)
```

---

## 🧪 测试覆盖

| 模块 | 用例文件 | 覆盖点 |
| --- | --- | --- |
| 登录 | `test_login.py` | 正确/错误凭证、多组校验、退出登录（登录态闭环） |
| 注册 | `test_register.py` | 表单校验 + 注册成功自动登录 |
| 商品 | `test_product.py` | 搜索、分类、无结果场景 |
| 详情 | `test_detail.py` | 名称 / 价格 / 库存 |
| 购物车 | `test_cart.py` | 加购、数量增减、删除、清空、合计 |
| 地址 | `test_address.py` | 收货信息表单校验 |
| 优惠券 | `test_coupon.py` | 满减券折后金额、未达门槛不打折 |
| 下单 | `test_order.py` | 完整下单流 + 动态金额校验 |
| 个人中心 | `test_user.py` | 登录态、订单列表 |

---

## 💬 说明

- 报告输出到 `reports/taotao_mall_report.html`，失败用例自带截图。
- `reports/` 为自动生成产物，已加入 `.gitignore`，不入库。
- 被测页面为纯前端 HTML，**零后端依赖**，克隆即可跑。