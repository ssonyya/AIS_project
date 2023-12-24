from application.config import SessionLocal
from application.services.repository_service import *
from application.GenerationData import GenerationData


""" Данный скрипт заполняет БД тестовыми данными """


if __name__ == "__main__":
    with SessionLocal() as session:
        car = GenerationData()
        #create_recommendation(session, info="Поменяйте тормозные колодки")

        #create_error(session, not_errors=True, error_acc=False, error_oil=False, error_fuel=False,
                    #error_temp=False, error_fuel_consumption=False, advice=4)
        create_car(session, car.getName(), car.getX(), car.getY(), car.getAccCharge(), car.getVolumeOil(),
                   car.getVolumeFuel(), car.getEngineTemp(), car.getFuelConsumption(), car.getMilease(), 1)

