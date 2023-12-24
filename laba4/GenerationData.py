import random

class GenerationData:
    def __init__(self):
        self.tank_volume = 400
        
        symbols = "ABEKMHOPCTYX"       
        self.name = str(random.randint(1, 9))
        for i in range(0, 3):
            self.name += symbols[random.randint(0, len(symbols) - 1)]
        self.name += str(random.randint(10, 99))

        self.x = random.uniform(0, 60)
        self.y = random.uniform(0, 60)

        self.acc_charge = random.randint(0, 100)
        self.volume_of_oil = random.randint(0, 100)
        self.volume_of_fuel = random.uniform(0, self.tank_volume)
        self.engine_temp = random.uniform(0, 130)
        self.fuel_consumption = random.uniform(0, 9999)
        self.milease = random.randint(0, 100)

    def getName(self):
        return self.name

    def getX(self):
        return round(self.x, 6)

    def getY(self):
        return round(self.y, 6)

    def getAccCharge(self):
        return self.acc_charge

    def getVolumeOil(self):
        return self.volume_of_oil

    def getVolumeFuel(self):
        return round(self.volume_of_fuel, 3)

    def getEngineTemp(self):
        return round(self.engine_temp, 3)

    def getFuelConsumption(self):
        return round(self.fuel_consumption, 2)

    def getMilease(self):
        return self.milease


if __name__ == '__main__':
    for i in range(0, 100):
        car = GenerationData()
        print(car.getName(), car.getX(), car.getY(), car.getAccCharge(), car.getVolumeOil(), car.getVolumeFuel(), car.getEngineTemp(), car.getFuelConsumption(), car.getMilease())
