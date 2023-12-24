from pydantic import BaseModel
from typing import (
    Deque, Dict, List, Optional, Sequence, Set, Tuple, Union
)

from datetime import datetime


class CarDTO(BaseModel):
    """ DTO для добавления, обновления и получения информации об автомобиле.
        Если данные, передаваемые клиенту сильно отличаются от данных,
        которые принимает REST API сервера, необходимо разделять DTO
        для запросов и ответов, например, CarRequestDTO, CarResponseDTO """
    name: str
    coord_x: float
    coord_y: float
    acc: int
    oil: int
    fuel: float
    temp: float
    fuel_consumption: float
    milease: int
    status: int
