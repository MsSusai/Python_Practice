class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.runMeter = 0
        self.gas = 0

    def getDescriptiveName(self):
        longName = str(self.year) + ' ' + self.make + ' ' + self.model
        return longName

    def readMeters(self):
        print("车行驶了{}公里".format(self.runMeter))
        return

    def updateMeters(self, updateMile):
        if updateMile >= self.runMeter:
            self.runMeter = updateMile
        else:
            print("不能将公里数向前变更！")
        return

    def plusMeters(self, plusMile):
        if plusMile >= 0:
            self.runMeter += plusMile
        else:
            print("不能将公里数向前变更！")
        return

    def fillGasTank(self, gas):
        self.gas += gas
        print("已加{}升油，目前有{}油".format(gas, self.gas))
        return


class Battery(object):
    def __init__(self, battery):
        self.batterySize = battery

    def describeBattery(self):
        print("电池容量为{}Kwh".format(self.batterySize))
        return


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery(70)

    def fillGasTank(self, gas):
        print("电动车不用加油！")
        return


# new_car = Car('audi', 'a4', 2016)
# print(new_car.getDescriptiveName())
# new_car.updateMeters(10)
# new_car.plusMeters(30)
# new_car.readMeters()

new_Electric_Car = ElectricCar('特斯拉', '2020最新款', 2020)
print(new_Electric_Car.getDescriptiveName())
new_Electric_Car.battery.describeBattery()
new_Electric_Car.updateMeters(20)
new_Electric_Car.readMeters()
new_Electric_Car.fillGasTank(20)
