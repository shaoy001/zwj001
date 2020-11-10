from lib import common
def login():
    print("登录功能")
    common.logger('egon刚刚登陆了')

def register():
    print("注册功能")

def witdraw():
    print("提现功能")

def transfer():
    print("转账功能")

func_dict={
    '0':['登录',login()],
    '1':['注册',register()],
    '2':['提现',witdraw()],
    '3':['转账',transfer()],
    '5':['退出',exit]
}

def run():
    while True:
        for k in  func_dict:
            print(k,func_dict[k][0])
        choice=input("请输入编号:").strip()
