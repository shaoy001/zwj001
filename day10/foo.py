x=1
def get():
    print(x)
def change():
    global x
    x+=100
    print(x)

if __name__ == '__main__':
    get()