# from ..core.src import run 错误，无法导入
import sys
import os
print(__file__) #当前文件的绝对路径
BASE_DIR=os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)
from  core import src



if __name__ == '__main__':
    src.run()