""" Market Schema """
"""_summary_
This file to abstract any validation logic for the Market
"""

from ast import Dict
from pydantic import BaseModel, validator

class MarketRequest(BaseModel):
    symbol: str

class MarketResponse(BaseModel):
    price: float

    @validator('price')
    def validate_not_zero(cls, value):
        if value <= 0 or None:
            raise ValueError("Price cannot be 0 or None.")
        return value

class MarketUserResponse(BaseModel):
    price_list: list[Dict[MarketRequest, MarketResponse]]
