import time
from  conf import setting
def logger(msg):
    with open(setting.LOG_PATH,mode='at',encoding='utf-8') as f:
        f.write('%s %s\n'%(time.strftime('%Y-%m-%d %H:%M:%S'),msg))