import json
from pathlib import Path

from parameterized import param


BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"


def read_json(file_path):
    """读取 JSON 文件，返回字典或列表"""
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"JSON 文件不存在: {file_path}")
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def get_data(filename):
    """读取 data/ 下指定 JSON 文件，转成 parameterized 所需的命名参数列表。

    JSON 文件须为「字典数组」，每个字典的键名与测试方法形参名一致，
    从而避免「数组位置对齐」带来的字段错位问题。

    例如 data/login.json:
        [{"username": "admin", "password": "123456", ...}, ...]

    返回：[param.explicit(kwargs=...), ...]，配合 @parameterized.expand 使用。
    """
    json_path = DATA_DIR / f"{filename}.json"
    data = read_json(json_path)

    if not isinstance(data, list):
        raise TypeError(f"数据文件须为 JSON 数组: {json_path}")

    return [param.explicit(kwargs=item) for item in data]