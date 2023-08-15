# 简单实现用户的注册、登陆、充值、购买


user = {}
user_ye = 0.0
dl = {}


def auth(self):
    def wrapper(*args, **kwargs):
        if not dl:
            print('请先登陆')
            return
        res = self(*args, **kwargs)
        return res
    return wrapper


def user_logon():
    while True:
        username = input('请输入用户名：')
        if username in user.keys():
            print('用户名已存在，请重新输入!')
            continue
        password = input('请输入密码：')
        user[username] = password
        print('注册成功')
        break
    print(f'您的帐号是：{username},密码是{password}，请牢记')
    # cz()


def user_login():
    while True:
        username = input('请输入用户名：').strip()
        password = input('请输入密码：').strip()
        try:
            if user[username] == password:
                dl[username] = password
                print('登陆成功！')
                break
            else:
                print('密码错误！')
                continue
        except KeyError:
            print('用户名有误，请重新输入')
            continue
    # cz()


@auth
def chongzhi():
    je = int(input('请输入要充值的金额：'))
    global user_ye
    ysye = user_ye
    user_ye += je
    print(f'充值成功！\n您原来的余额为：{ysye}，本次充值：{je}，现在余额为：{user_ye}')


@auth
def goumai():
    global user_ye
    sp = {
        '001': ['卫生纸', '5.00'],
        '002': ['洗发水', '20.00'],
        '003': ['毛巾', '15.00']
    }
    for k, v in sp.items():
        print(f'{v[0]}(编号：{k})--->价格：{v[1]}')
    gmje = 0
    gwc = {}
    while True:
        gmsp = input('请选择要购买商品编号:')
        if gmsp not in sp.keys():
            print('没有此商品，重新选择')
            continue
        gmsl = int(input('请输入数量'))
        gmje += float(sp[gmsp][1])*gmsl
        gwc[sp[gmsp][0]] = [gmsl, float(sp[gmsp][1])*gmsl]
        isjx = input('是否继续购买？Y/N')
        if isjx.upper() == 'N':
            break
    print('您本次购买的商品有:')
    for k, v in gwc.items():
        print(k, v)
    print('总金额：', gmje)
    isjs = input('是否去结算？Y/N')
    if isjs.upper() == 'N':
        return
    while user_ye < gmje:
        print('余额不足，请充值')
        chongzhi()
    user_ye -= gmje
    print(f'结算成功，本次消费：{gmje}，余额{user_ye}')


ts = {
    '0': ('注册：', user_logon),
    '1': ('登陆：', user_login),
    '2': ('充值：', chongzhi),
    '3': ('购买：', goumai),
    'Q': ('退出：', None)
}


def cz():
    while True:
        for k, v in ts.items():
            print(v[0], k)
        cz = input('请输入操作：')
        try:
            if cz == 'q' or cz == 'Q':
                break
            ts[cz][1]()
        except KeyError:
            print('输入有误，请重新输入')


if __name__ == '__main__':
    cz()
