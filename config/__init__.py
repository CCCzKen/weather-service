import os
from importlib import import_module


MODE = os.environ.get('MODE') or 'dev'


try:
    current_config = import_module('config.' + MODE)
except ImportError:
    print('[!] 配置错误，请初始化环境变量')
