# 创建一个单例对象
class MusicPlayer(object):
    # 定义一个类属性
    instance = None
    # 定义个类属性，记录是否执行过初始化操作
    init_flag = False

    # 重写new方法
    def __new__(cls, *args, **kwargs):
        # 判断当前的类属性是否为空对象
        if cls.instance is None:
            # 如果为空，就调用父类方法为第一个对象分配内存空间
            cls.instance = super().__new__(cls)
        # 返回类属性保存的对象的引用
        return cls.instance

    # 初始化动作只执行一次
    def __init__(self):
        # 首先判断初始化动作的标志是否为真，为真就直接返回，不再执行初始化
        if MusicPlayer.init_flag:
            return
        print("播放器初始化...")
        # 初始化过后，将标志置为True
        MusicPlayer.init_flag = True


# 创建多个对象的实例
player1 = MusicPlayer()
print(player1)
player2 = MusicPlayer()
print(player2)
