from typing import Optional, Iterable, List
from sqlalchemy.orm import Session
from application.models.dao import *
import functools
import traceback


def dbexception(db_func):
    """ Функция-декоратор для перехвата исключений БД.
        Данный декоратор можно использовать перед любыми
        функциями, работающими с БД, чтобы не повторять в
        теле функции конструкцию try-except (как в функции add_weather). """
    @functools.wraps(db_func)
    def decorated_func(db: Session, *args, **kwargs) -> bool:
        try:
            db_func(db, *args, **kwargs)    # вызов основной ("оборачиваемой") функции
            db.commit()     # подтверждение изменений в БД
            return True
        except Exception as ex:
            # выводим исключение и "откатываем" изменения
            print(f'Exception in {db_func.__name__}: {traceback.format_exc()}')
            db.rollback()
            return False
    return decorated_func


def get_car_by_name(db: Session, name: str) -> Optional[Car]:
    """ Выбор записи об автомобиле по его номеру (PRIMARY KEY)"""
    result = db.query(Car).filter(Car.name == name).first()
    return result

def get_car_name(db: Session) -> str:
    """ Получение всех доступных номеров автомобилей"""
    result = db.query(Car.name).all()
    return result


def get_car_by_status(db: Session, status: int) -> Iterable[Car]:
    """ Выборка всех записей об автомобилях по статусу ошибки """
    result = db.query(Car).filter(Car.status == status).all()
    return result


def get_error_by_recommendation(db: Session, info: str) -> Iterable[Errors]:
    """ Выбор всех записей об ошибоках в автомобилях по рекоммендации для устранения этой ошибки """
    result = db.query(Errors).join(Recommendation).filter(Recommendation.info == info).all()
    return result


def get_error_by_id(db: Session, id: int) -> Optional[Errors]:
    """ Выбор записи об ошибке в автомобиле по его индентификатору (PRIMARY KEY) """
    result = db.query(Errors).filter(Errors.id == id).first()
    return result


def get_recommendation_by_id(db: Session, id: int) -> Optional[Recommendation]:
    """ Выбор записи об рекоммендации по устранению ошибки в автомобиле по индентификатору (PRIMARY KEY) """
    result = db.query(Recommendation).filter(Recommendation.id == id).first()
    return result


def get_recommendation_by_info(db: Session, info: str) -> Optional[Recommendation]:
    """ Выбор записи об рекоммендации по устранению ошибки в автомобиле по содержанию этой рекоммендации """
    result = db.query(Recommendation).filter(Recommendation.info == info).first()
    return result


def create_car(db: Session, name: str, coord_x: float, coord_y: float, acc: int, oil: int, fuel: float, temp: float, fuel_consumption: float, milease: int, status: int) -> bool:
    """ Создание нового объекта Car и добавление записи об автомобиле """
    car = Car(
        name=name,
        coord_x=coord_x,
        coord_y=coord_y,
        acc=acc,
        oil=oil,
        fuel=fuel,
        temp=temp,
        fuel_consumption=fuel_consumption,
        milease=milease,
        status=status
        )
    return add_car(db, car)


def create_error(db: Session, not_errors: bool, error_acc: bool, error_oil: bool, error_fuel: bool, error_temp: bool, error_fuel_consumption: bool, advice: int) -> bool:
    """ Создание нового объекта Error и добавление записи об ошибке автомобиля"""
    error = Errors(
        not_errors=not_errors,
        error_acc=error_acc,
        error_oil=error_oil,
        error_fuel=error_fuel,
        error_temp=error_temp,
        error_fuel_consumption=error_fuel_consumption,
        advice=advice
        )
    return add_error(db, error)


def create_recommendation(db: Session, info: str) -> bool:
    """ Создание нового объекта Recommendation и добавление записи рекоммендации для ошибки"""
    recomm = Recommendation(
        info=info
        )
    return add_recommendation(db, recomm)


def add_car(db: Session, car: Car) -> bool:
    """ Добавление записи об автомобиле (с помощью готового объекта Car) """
    try:
        db.add(car)
        db.commit()
    except Exception as ex:
        print(traceback.format_exc())
        db.rollback()
        return False
    return True


def add_error(db: Session, error: Errors) -> bool:
    """ Добавление записи об ошибке (с помощью готового объекта Error) """
    try:
        db.add(error)
        db.commit()
    except Exception as ex:
        print(traceback.format_exc())
        db.rollback()
        return False
    return True


def add_recommendation(db: Session, recomm: Recommendation) -> bool:
    """ Добавление записи об рекоммендации (с помощью готового объекта Recommendation) """
    try:
        db.add(recomm)
        db.commit()
    except Exception as ex:
        print(traceback.format_exc())
        db.rollback()
        return False
    return True


@dbexception
def delete_car_by_name(db: Session, name: str) -> bool:
    """ Удаление записей об автомобиле по его номеру """
    car = get_car_by_name(db, name)
    db.delete(car)


def update_error_in_car_by_name(db: Session, id_error: int, name: str) -> bool:
    """ Обновление статуса ошибки у автомобиля """
    car = get_car_by_name(db, name)
    car.status = id_error
    return add_car(db, car)


def update_milease_in_car_by_name(db: Session, milease: int, name: str) -> bool:
    """ Обновление пробега у автомобиля """
    car = get_car_by_name(db, name)
    car.milease = milease
    return add_car(db, car)
