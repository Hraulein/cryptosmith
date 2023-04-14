"""
生成随机密码
"""
import random
import string
from enum import Enum


class Cipher(Enum):
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


def random_password(bit: int, level: Cipher, number: int = 1):
    """
    生成随机密码
    :param bit: 生成密码的位数: 最低8位
    :param level: 密码强度等级: Cipher(Enum)
    :param number: 生成的密码个数
    :return: 随机密码
    """
    def random_choice(string_type: str):
        """
        抓取随机字符串生成密码
        :type string_type: str
        :param string_type: 密码等级对应的随机字符串
        :return:
        """
        result = []
        for i in range(number):
            for j in range(bit):
                char = random.choice(string_type)
                result.append(char)
            if i < number:
                result.append('\n')
        return ''.join(result)

    # 输入判断
    if bit < 8 or number < 1:
        if bit < 8:
            print('输入的密码位数小于8, 已自动设置为8')
            bit = 8
        if number < 1:
            print('输入的密码个数小于1, 已自动设置为1')
            number = 1
    # 随机字符生成
    letters = random.sample(string.ascii_letters, 40)
    lowercase = random.sample(string.ascii_lowercase, 20)
    uppercase = random.sample(string.ascii_uppercase, 20)
    digits = random.sample(string.digits, 10) + random.sample(string.digits, 10)
    # symbols = list('!@#$%^&*()_+-=[]{}><?')
    symbols = list('!@#$%&*_+-=<>?')
    match level:
        case Cipher.simple:
            # 随机数字
            password = random_choice(digits)
        case Cipher.commonly:
            # 随机数字 + 随机小写字母
            password = random_choice(digits + lowercase)
        case Cipher.routine:
            # 随机数字 + 随机大写字母
            password = random_choice(digits + uppercase)
        case Cipher.recommend:
            # 随机数字 + 随机大小写字母
            password = random_choice(digits + letters)
        case Cipher.strong:
            # 随机数字 + 随机大小写字母 + 特殊符号
            password = random_choice(digits + letters + symbols)
        case _:
            print('密码等级错误, 正确密码等级应为 Cipher(Enum)')
            exit(-999)
    return password


if __name__ == '__main__':
    for k in range(len(Cipher)):
        print(f'【{Cipher(k + 1)}】')
        print(random_password(30, Cipher(k + 1), 5))
