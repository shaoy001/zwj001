import time
def logger():
    with open(r'user.log',mode='at',encoding='utf-8') as f:
        f.write('%s %s\n'%(time.strftime(%Y-%m-%d %H:%M:%S),msg))
