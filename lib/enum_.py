"""
枚举类
"""
from enum import Enum


class Level(Enum):
    """
    密码强度等级
    :var simple: 简单
    :var commonly: 一般
    :var routine: 普通
    :var recommend: 推荐
    :var strong: 强
    """
    simple = 1
    commonly = 2
    routine = 3
    recommend = 4
    strong = 5


class CKey(Enum):
    """
    配置文件的 key
    """
    level = 1,
    count = 2,
    bit = 3
