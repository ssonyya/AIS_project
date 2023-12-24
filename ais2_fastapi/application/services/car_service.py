from typing import Optional, List
from application.config import SessionLocal
from application.models.dao import Car
from application.models.dto import CarDTO, RecommendationDTO
import application.services.repository_service as repository_service


"""

    Данный модуль содержит программный слой с реализацией дополнительной бизнес-логики, 
    выполняемой перед или после выполнения операций над хранилищем данных (repository), 
    например: маппинг атрибутов из DAO в DTO, применение дополнительных функций к атрибутам DTO.
    
    ВАЖНО! Реализация данного слоя приведена в качестве демонстрации полной структуры RESTful веб-сервиса.
           В небольших проектах данный слой может быть избыточен, в таком случае, из контроллера ваших маршрутов 
           (Router в FastAPI или View в Django) можно напрямую работать с функциями хранилища данных (repository_service).

"""


class CarService:

    def get_car_by_number(self, name: str) -> Optional[CarDTO]:
        result = None
        with SessionLocal() as session:     # конструкция with позволяет автоматически завершить сессию после выхода из блока
            result = repository_service.get_car_by_name(session, name)
        if result is not None:
            return self.map_car_data_to_dto(result)
        return result

    def get_all_car_by_status(self, status: int) -> List[CarDTO]:
        car_data: List[CarDTO] = []
        with SessionLocal() as session:
            result = repository_service.get_car_by_status(session, status)
            for w in result:
                car_data.append(self.map_car_data_to_dto(w))
        return car_data

    def add_car_info(self, car: CarDTO) -> bool:
        with SessionLocal() as session:
            return repository_service.create_car(session,
                                                 name=car.name,
                                                 coord_x=car.coord_x,
                                                 coord_y=car.coord_y,
                                                 acc=car.acc,
                                                 oil=car.oil,
                                                 fuel=car.fuel,
                                                 temp=car.temp,
                                                 fuel_consumption=car.fuel_consumption,
                                                 milease=car.milease,
                                                 status=car.status)

    def update_error_in_car(self, name: str, status: int) -> bool:
        with SessionLocal() as session:
            return repository_service.update_error_in_car_by_name(session, id_error=status, name=name)

    def update_milease_in_car(self, name: str, milease: int) -> bool:
        with SessionLocal() as session:
            return repository_service.update_milease_in_car_by_name(session, milease=milease, name=name)

    def delete_car_info_by_name(self, name: str) -> bool:
        with SessionLocal() as session:
            return repository_service.delete_car_by_name(session, name)

    def get_car_all_name(self) -> List[str]:
        car_data: List[str] = []
        with SessionLocal() as session:
            result = repository_service.get_car_name(session)
            for w in result:
                car_data.append(w[0])
        print(car_data)
        return car_data

    def get_recommendation(self, id: int) -> Optional[RecommendationDTO]:
        with SessionLocal() as session:
            result = repository_service.get_recommendation_by_id(session, id)
        return result

    def add_recommendation(self, recommendation: RecommendationDTO) -> bool:
        if recommendation.info != "":
            with SessionLocal() as session:
                return repository_service.create_recommendation(session, info=recommendation.info)
        return False

    def map_car_data_to_dto(self, car_dao: Car):
        """ Метод для конвертирования (маппинга) Car DAO в CarDTO """
        return CarDTO(name=car_dao.name,
                      coord_x=car_dao.coord_x,
                      coord_y=car_dao.coord_y,
                      acc=car_dao.acc,
                      oil=car_dao.oil,
                      fuel=car_dao.fuel,
                      temp=car_dao.temp,
                      fuel_consumption=car_dao.fuel_consumption,
                      milease=car_dao.milease,
                      status=car_dao.status)
