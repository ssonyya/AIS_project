from pydantic import BaseModel


class RecommendationDTO(BaseModel):
    """ DTO для добавления новой рекоммендации по устранению ошибки в автомобиле """
    info: str
