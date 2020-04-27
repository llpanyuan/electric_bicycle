"""
写一个Bicycle（自行车）类，有run（骑行）方法，调用时显示骑行里程km（骑行里程为传入的数字）：
再写一个电动自行车类EBicycle继承自Bicycle，添加电池电量valume属性通过参数传入，同时有两个方法：
1.fill_charge（vol）用来充电，vol为电量（度）
2.run（km）方法用于骑行，每骑行10km消耗电量1度，当电量消耗尽时调用Bicycle的run方法骑行，通过传入的骑行里程数，显示骑行结果
"""


# 定义自行车类
class Bicycle:
    # 定义自行车方法
    def run(self, km):
        print("骑行里程：{}".format(km))


# 定义电动自行车类
class EBicycle(Bicycle):
    # 初始化，传入电池电量，默认为10
    def __init__(self, valume=10):
        self.valume = valume

    # 定义充电方法，默认为0，没充电
    def fill_charge(self, vol=0):
        self.valume = vol + self.valume
        print("电动车当前电量为：", self.valume)

    # 定义电动自行车骑行方法
    def run(self, km):
        # 打印目标里程数
        print("目标里程：", km)
        # 调用充电方法，获取当前准确电量
        self.fill_charge()
        # 电动车电量最大支持的里程数：电动车电量的10倍
        e_mileage = self.valume * 10
        # 使用自行车骑里程数
        mileage = km - e_mileage
        # 判断是否需要使用人力骑行
        if mileage <= 0:
            print("电动车骑了{}公里".format(km))
        elif mileage > 0:
            print("电瓶车骑了：", e_mileage)
            super().run(mileage)


# 电动车类实例化
ebicycle = EBicycle()
ebicycle.run(200)
