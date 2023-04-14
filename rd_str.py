"""
生成随机字符串(密码)
"""
from lib.utils_ import random_string
from lib.enum_ import Level
from lib.config_ import YamlConfig


def _config_verity_value(key, value, limit=None) -> bool:
    """
    验证key的value是否合规
    :param value: key的值
    """
    pass


if __name__ == '__main__':
    yml = YamlConfig('config/config.yml', 'RD_STR')
    config = yml.loaded_config()

    try:
        print(random_string(Level(config['level']), config['count'], config['bit']))
        pass
    except ValueError:
        print('配置文件的 level 值有误, 正确值应为 1-5')
    """
    # 打印全部级别的密码
    for i in range(len(Level)):
        print(f'【{Level(i + 1)}】')
        print(random_string(Level(i + 1), config['count'], config['bit']))
    """

