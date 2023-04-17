"""
工具类
"""
import os
import random
import string

from lib import enum_


def random_string(cipher: enum_.Level, count: int = 1, bit: int = 8) -> str:
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
    symbols = list('!?@#$%&*_+-=<>')
    match cipher:
        case enum_.Level.simple:
            # 随机数字
            return _random_choice(digits)
        case enum_.Level.commonly:
            # 随机数字 + 随机小写字母
            return _random_choice(digits + lowercase)
        case enum_.Level.routine:
            # 随机数字 + 随机大写字母
            return _random_choice(digits + uppercase)
        case enum_.Level.recommend:
            # 随机数字 + 随机大小写字母
            return _random_choice(digits + letters)
        case enum_.Level.strong:
            # 随机数字 + 随机大小写字母 + 特殊符号
            return _random_choice(digits + letters + symbols)


def create_file(filepath, value=None):
    """
    创建文件(如果文件不存在)
    :param filepath: 文件路径
    :param value: 要写入的值
    :return: bool: 创建成功true 创建失败 false
    """
    folder = os.path.dirname(filepath)
    if not os.path.exists(filepath):
        if not os.path.exists(folder):
            os.makedirs(folder)
        with open(filepath, 'w') as f:
            if value is not None:
                f.write(value)
        return True
    else:
        return False


def console_pause():
    """
    控制台不关闭
    """
    os.system('pause')
