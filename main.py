import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))

from scripts.test_login import TestLogin
from scripts.test_product import TestProduct
from scripts.test_detail import TestDetail, TestDetailRich
from scripts.test_cart import TestCart
from scripts.test_address import TestAddress
from scripts.test_order import TestOrder
from scripts.test_user import TestUser
from scripts.test_register import TestRegister
from scripts.test_coupon import TestCoupon
from scripts.test_shop import TestShop, TestShopReverse
from scripts.test_user_center import TestUserCenter, TestUserCenterReverse
from scripts.test_address_manage import TestAddressManage
from scripts.test_pagination import TestPagination
from scripts.test_seller_center import TestSellerCenter, TestSellerCenterReverse
from scripts.test_messages import TestMessages, TestMessagesReverse
from scripts.test_info_modals import TestFooterLink, TestAgreement
from scripts.test_unauthorized import TestUnauthorized, TestRegisterLinkLifecycle
from scripts.test_banner import TestBanner
from scripts.test_coupon_my import TestMyCoupons, TestMyCouponsReverse

from XTestRunner import HTMLTestRunner
from base.get_driver import GetDriver


def main():
    report_dir = ROOT / "reports"
    report_dir.mkdir(exist_ok=True)
    report_path = report_dir / "taotao_mall_report.html"

    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    for cls in [TestLogin, TestRegister, TestProduct, TestDetail, TestDetailRich, TestCart,
                TestAddress, TestOrder, TestCoupon, TestUser,
                TestShop, TestShopReverse, TestUserCenter, TestUserCenterReverse,
                TestAddressManage, TestPagination,
                TestSellerCenter, TestSellerCenterReverse, TestMessages, TestMessagesReverse,
                TestFooterLink, TestAgreement, TestUnauthorized, TestRegisterLinkLifecycle,
                TestBanner, TestMyCoupons, TestMyCouponsReverse]:
        suite.addTest(loader.loadTestsFromTestCase(cls))

    with open(report_path, "wb") as fp:
        runner = HTMLTestRunner(
            stream=fp,
            title="淘淘商城 自动化测试报告",
            description="测试环境：本地 Chrome | 测试页面：淘淘商城.html",
            language="zh-CN",
            tester="forminio"
        )
        runner.run(suite)

    # 全部用例执行完毕后统一退出浏览器（而非每个测试类各启停一次）
    GetDriver().quit_driver()

    print(f"报告已生成: {report_path}")


if __name__ == "__main__":
    main()