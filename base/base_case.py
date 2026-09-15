import unittest

from base.get_driver import GetDriver


class BaseCase(unittest.TestCase):
    """统一测试基类。

    职责：
    1. setUpClass 统一获取全局单例浏览器驱动；
    2. setUp 重新加载页面，重置 JS 内存状态（购物车/订单/登录态），保证用例独立。

    说明：失败截图由 XTestRunner 生成 HTML 报告时自动完成
    （检测到用例存在 WebDriver 且失败时，自动 base64 截图内嵌进报告），
    因此本基类不再做手动截图。
    """

    @classmethod
    def setUpClass(cls):
        cls.driver = GetDriver().get_driver()

    def setUp(self):
        self.driver.get(GetDriver().get_url())