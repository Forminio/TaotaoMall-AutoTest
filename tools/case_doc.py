"""parameterized 用例的 doc_func，让测试报告中的「描述」列更干净。

默认情况下 parameterized 会把参数展开成 "[with xxx=yyy]" 追加到 docstring 后，
在报告中显得杂乱；此函数直接返回测试方法 docstring 的首行作为用例描述。
"""


def case_doc(func, num, p):
    doc = (func.__doc__ or "").lstrip().split("\n")[0].strip()
    return doc or None