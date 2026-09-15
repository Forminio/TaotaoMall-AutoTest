"""金额格式化/解析，与 demo 页面的 formatPrice 逻辑保持一致。"""


def format_price(n):
    """数字转千分位字符串：8999 -> '8,999'（与 demo 的 formatPrice 一致）"""
    return f"{int(n):,}"


def parse_price(text):
    """从价格文本中提取整数：'¥8,999' / '8,999' -> 8999"""
    digits = "".join(ch for ch in str(text) if ch.isdigit())
    return int(digits) if digits else 0