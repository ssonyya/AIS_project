import unittest
import random
from application.config import SessionLocal
from application.services.repository_service import *
from application.GenerationData import GenerationData


"""
   Данный модуль реализует "тестовые случаи/ситуации" для модуля repository_service.
   Для создания "тестового случая" необходимо создать отдельный класс, который наследует 
   базовый класс TestCase. Класс TestCase предоставляется встроенным 
   в Python модулем для тестирования - unittest.
   
   Более детально см.: https://pythonworld.ru/moduli/modul-unittest.html
"""


class TestWeatherRepositoryService(unittest.TestCase):
    """ Все тестовые методы в классе TestCase (по соглашению)
        должны начинаться с префикса test_* """

    def setUp(self):
        """ Наследуемый метод setUp определяет инструкции,
            которые должны быть выполнены ПЕРЕД тестированием """
        self.session = SessionLocal() # создаем сессию подключения к БД
        try:
            recomm = Recommendation(
                info="Всё плохо"
            )
            add_recommendation(self.session, recomm)

            error = Errors(
                not_errors=False,
                error_acc=True,
                error_oil=True,
                error_fuel=False,
                error_temp=True,
                error_fuel_consumption=False,
                advice=1
            )
            add_error(self.session, error)
        except:
            print('Test data already created')

    def test_create_car(self):
        """ Тест функции создания записи Car """
        car = GenerationData()
        result = create_car(self.session, name="r777ok", coord_x=car.getX(), coord_y=car.getY(),
                            acc=car.getAccCharge(), oil=car.getVolumeOil(), fuel=car.getVolumeFuel(),
                            temp=car.getEngineTemp(), fuel_consumption=car.getFuelConsumption(),
                            milease=car.getMilease(), status=1)
        self.assertTrue(result)     # валидируем результат (result == True)

    def test_get_car(self):
        """ Тест функции поиска записи Car по его номеру """
        car = get_car_by_name(self.session, name="5PTB95")
        self.assertIsNotNone(car)           # запись должна существовать
        self.assertTrue(car.name == "5PTB95")

    def test_get_car_by_recommendation(self):
        """ Тест функции поиска записи Car по его номеру """
        errors = get_error_by_recommendation(self.session, info="Всё плохо")
        for error in errors:
            cars = get_car_by_status(self.session, status=error.id)
            self.assertIsNotNone(error)           # запись должна существовать
            for car in cars:
                self.assertIsNotNone(car)  # запись должна существовать
                self.assertTrue(car.status == error.id)


    def test_delete_car(self):
        """ Тест функции удаления записи Car по номеру """
        delete_car_by_name(self.session, name="r777ok")
        result = get_car_by_name(self.session, name="r777ok")
        self.assertIsNone(result)       # запись не должна существовать

    def tearDown(self):
        """ Наследуемый метод tearDown определяет инструкции,
            которые должны быть выполнены ПОСЛЕ тестирования """
        self.session.close()        # закрываем соединение с БД

    def testUpdate(self):
        update_error_in_car_by_name(self.session, 1, "5PTB95")


if __name__ == '__main__':
    unittest.main()
