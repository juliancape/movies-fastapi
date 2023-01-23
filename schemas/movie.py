from pydantic import BaseModel
from typing import Optional
from pydantic import Field


#Esquemas
class Movie(BaseModel):
    id: Optional[int] = None
    title: str = Field(min_length=5 ,max_length=20)
    overview: str = Field(min_length=15 ,max_length=55)
    year: int = Field(le=2023)
    rating: float = Field(ge=0.0,le=10.0)
    category: str = Field(min_length=3 ,max_length=15)

    class Config:
        schema_extra = {
            'example': {
                'title': 'Mi película',
                'overview': 'Descripción de la película',
                'year': 2023,
                'rating': 0.1,
                'category': 'None'
            }
        }