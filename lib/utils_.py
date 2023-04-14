"""
工具类
"""
import random
import string
from os import path, makedirs

from lib.enum_ import Level


def random_string(cipher: Level, count: int = 1, bit: int = 8) -> str:
    """
    创建随机字符
    :param cipher:
    :param count:
    :param bit:
    """
    def _random_choice(str):
        """
        抓取字符生成随机字符串
        :type str: str
        :return:
        """
        result = []
        for i in range(count):
            for j in range(bit):
                char = random.choice(str)
                result.append(char)
            if i < count:
                result.append('\n')
        return ''.join(result)
    letters = random.sample(string.ascii_letters, 40)
    lowercase = random.sample(string.ascii_lowercase, 20)
    uppercase = random.sample(string.ascii_uppercase, 20)
    digits = random.sample(string.digits, 10) + random.sample(string.digits, 10)
    # symbols = list('!@#$%^&*()_+-=[]{}><?')
    symbols = list('!@#$%&*_+-=<>?')
    match cipher:
        case Level.simple:
            # 随机数字
            return _random_choice(digits)
        case Level.commonly:
            # 随机数字 + 随机小写字母
            return _random_choice(digits + lowercase)
        case Level.routine:
            # 随机数字 + 随机大写字母
            return _random_choice(digits + uppercase)
        case Level.recommend:
            # 随机数字 + 随机大小写字母
            return _random_choice(digits + letters)
        case Level.strong:
            # 随机数字 + 随机大小写字母 + 特殊符号
            return _random_choice(digits + letters + symbols)
        case _:
            print('密码等级错误, 正确密码等级应为 1-5')
            return ''


def create_file(filepath, value=None):
    """
    创建文件(如果文件不存在)
    :param filepath: 文件路径
    :param value: 要写入的值
    :return: bool: 创建成功true 创建失败 false
    """
    folder = path.dirname(filepath)
    if not path.exists(filepath):
        if not path.exists(folder):
            makedirs(folder)
        with open(filepath, 'w') as f:
            if value is not None:
                f.write(value)
        return True
    else:
        return False
