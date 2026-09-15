import os
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class GetDriver:
    """浏览器驱动单例：整个测试进程只创建一次 Chrome，避免反复启停。"""

    driver = None
    url = None

    @classmethod
    def get_driver(cls):
        if cls.driver is None:
            options = Options()
            # 设置 HEADLESS=1 时以无头模式运行（便于 CI / 无人值守）
            if os.getenv("HEADLESS") == "1":
                options.add_argument("--headless=new")
                options.add_argument("--disable-gpu")
                options.add_argument("--window-size=1920,1080")

            cls.driver = webdriver.Chrome(options=options)
            if os.getenv("HEADLESS") != "1":
                cls.driver.maximize_window()

            cls.driver.get(cls.get_url())
        return cls.driver

    @classmethod
    def get_url(cls):
        if cls.url is None:
            base = Path(__file__).resolve().parent.parent
            cls.url = (base / "demo" / "淘淘商城.html").as_uri()
        return cls.url

    @classmethod
    def quit_driver(cls):
        if cls.driver is not None:
            cls.driver.quit()
        cls.driver = None