"""
生成随机字符串(密码)
"""
from lib import config_, enum_, utils_


if __name__ == '__main__':
    yml = config_.YamlConfig('config/config.yml', 'RD_STR')
    config = yml.loaded_config()
    # 打印配置文件级别的密码
    print(utils_.random_string(enum_.Level(config['level']), config['count'], config['bit']))
    # 打印全部级别的密码
    # for i in range(len(enum_.Level)):
    #     print(f'【{enum_.Level(i + 1)}】')
    #     print(utils_.random_string(enum_.Level(i + 1), config['count'], config['bit']))

    utils_.console_pause()
