"""
校验配置文件, 提供默认值
"""
import datetime

import yaml
from os import path
import lib.utils_
from lib.enum_ import CKey


class YamlConfig:
    """
    配置文件yaml格式, 检查配置文件是否存在, 值是否正确
    """
    _INFO = {
        'root': 'INFO',
        'auther': 'Ali',
        'email': 'solitude@hraulein.com',
        'site': 'https://hraulein.com',
        'create': datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S'),
        'version': '1.0.0'
    }
    _RD_STR = {
        'root': 'RD_STR',
        'level': '!!int 5',
        'count': '!!int 1',
        'bit': '!!int 16'
    }

    def __init__(self, file, root):
        self.f = file
        self.r = root

    @staticmethod
    def _dict_to_yaml(_dict: dict) -> str:
        """
                dict转为yaml格式, 过滤 dict 的 root 字段
                :param _dict: 字典
                :return: yaml格式字符串
                """
        result = f"{_dict['root']}:\n"
        for i, j in _dict.items():
            if i != 'root':
                result += f'  {i}: {j}\n'
        return result + '\n'

    def _config_default_value(self) -> str:
        """
        提供配置文件默认值
        :return: 配置文件默认值(yaml文本格式)
        """
        _start = '%YAML 1.2\n---\n'
        _end = '...\n'
        return f"{_start}" \
               f"{self._dict_to_yaml(self._INFO)}" \
               f"{self._dict_to_yaml(self._RD_STR)}" \
               f"{_end}"

    def _config_default_write(self):
        """
        写入默认配置到yaml文件
        """
        with open(self.f, 'w', encoding='utf-8') as yml:
            yml.write(self._config_default_value())

    def _config_file_exists(self) -> bool:
        """
        确认配置文件是否存在
        :return: bool
        """
        return True if path.exists(self.f) else False

    def _config_read_yaml(self):
        """
        读取配置文件
        :return: 读取的配置文件值, yaml.load
        """
        # with open(self.f, 'r', encoding='utf-8') as yml:
        #     res = yaml.load(yml, yaml.FullLoader)
        yml = open(self.f, 'r', encoding='utf-8')
        config = yaml.load(yml, yaml.FullLoader)
        yml.close()
        return config

    def _config_verity_root(self, yml) -> bool:
        """
        验证配置文件的根是否正确
        :param yml: 读取的 yaml.load 值
        :return: 正确返回 true, 错误返回 false
        """
        try:
            var = yml[self.r]
            return True
        except KeyError:
            return False

    def _config_verity_key(self) -> bool:
        """
        验证key是否与默认值相匹配
        """
        default_list = []
        config_list = []
        for i in self._RD_STR.keys():
            if i != 'root':
                default_list.append(i)
        for j in self._config_read_yaml()[self.r].keys():
            config_list.append(j)
        return sorted(config_list) == sorted(default_list)

    def _config_verity_value(self) -> bool:
        """
        验证key的value是否合规
        :param value: key的值
        """
        _bool = []

        conf = self._config_read_yaml()[self.r]
        if isinstance(conf[CKey.level.name], int):
            if 1 <= conf[CKey.level.name] <= 5:
                _bool.append(True)
        if isinstance(conf[CKey.count.name], int):
            if 1 <= conf[CKey.count.name]:
                _bool.append(True)
        if isinstance(conf[CKey.bit.name], int):
            if 8 <= conf[CKey.bit.name]:
                _bool.append(True)

    def _config_failed_fix(self, _bool: bool, _exit: int, tips):
        """
        配置文件错误修复
        :param _bool: 配置文件的验证结果
        :type _exit: 程序退出代码
        :param tips: 配置错误提示
        """
        if not _bool:
            self._config_default_write()
            print(tips)
            exit(_exit)

    def loaded_config(self):
        """
        读取配置文件
        - 如果不存在则写入后再次读取
        - 如果配置文件根错误, 重置配置文件
        - 如果配置文件key错误, 重置配置文件
        - 如果配置文件key的值错误, 重置配置文件
        :return: 返回带有正确配置文件的dict
        """
        # 配置文件不存在
        if not self._config_file_exists():
            lib.utils_.create_file(self.f, self._config_default_value())
        conf = self._config_read_yaml()
        vc_root = self._config_verity_root(conf)
        # 配置文件根错误
        self._config_failed_fix(self._config_verity_root(conf), -1, '配置文件错误已重置, 请重启程序')
        # 配置文件key错误 (比较两个列表)
        self._config_failed_fix(self._config_verity_key(), -2, '配置文件key错误已重置, 请重启程序')
        # 返回带有正确配置文件的dict
        return conf[self.r]
