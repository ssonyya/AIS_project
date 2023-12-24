from fastapi import APIRouter, HTTPException, status, Request, Response
from starlette.responses import RedirectResponse
from application.models.dto import *
from application.services.car_service import CarService


"""

    Данный модуль отвечает за маршрутизацию доступных API URI (endpoints) сервера

"""


router = APIRouter(prefix='/api', tags=['Car Forecast API'])       # подключаем данный роутер к корневому адресу /api
service = CarService()              # подключаем слой с дополнительной бизнес-логикой


@router.get('/')
async def root():
    """ Переадресация на страницу Swagger """
    return RedirectResponse(url='/docs', status_code=307)


@router.get('/car/{errors_id}', response_model=List[CarDTO])
async def get_all_car_by_errors(errors_id: int):
    """ Получение всех записей об автомобиле по статусу его ошибки """
    return service.get_all_car_by_status(errors_id)


@router.get('/car', response_model=CarDTO)
async def get_car_by_name(name: str):
    """ Получение записи об автомобиле по его госномеру """
    response = service.get_car_by_number(name)
    if response is None:
        return Response(status_code=204)
    return response


@router.post('/car', status_code=201)
async def post_car(car: CarDTO):
    """ Добавить новую запись об автомобиле """
    if service.add_car_info(car):
        return Response(status_code=201)
    else:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Can't add new Car data",
        )


@router.put('/car', status_code=202)
async def put_car(name: str, status: int):
    """ Обновить статус ошибки у автомобиля """
    if service.update_error_in_car(name=name, status=status):
        return Response(status_code=202)
    else:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Can't update Car data",
        )


@router.put('/carmil', status_code=202)
async def put_car_milease(name: str, milease: int):
    """ Обновить пробег у автомобиля """
    if service.update_milease_in_car(name=name, milease=milease):
        return Response(status_code=202)
    else:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Can't update Car data",
        )


@router.get('/carnamme', response_model=List[str])
async def get_car_name():
    """ Получение всех доступных госномеров автомобилей """
    return service.get_car_all_name()

@router.get('/rectext', response_model=RecommendationDTO)
async def get_rec_text(id: int):
    """ Получение рекоомендации по id """
    return service.get_recommendation(id)


@router.delete('/car/{name}', status_code=200)
async def del_car(name: str):
    """ Удаление записи об автомобиле по его госномеру """
    if service.delete_car_info_by_name(name):
        return Response(status_code=200)
    else:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Can't delete Car data",
        )


@router.post('/recommendation', status_code=201)
async def create_recommendation(recomm: RecommendationDTO) -> Response:
    """ Добавить новую рекоммендация по устранению ошибки в автомобиле """
    if service.add_recommendation(recomm):
        return Response(status_code=201)
    else:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Can't add new Recommendation data",
        )
