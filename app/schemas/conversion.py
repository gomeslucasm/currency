from pydantic import BaseModel, Field
from typing import Literal

ALLOWED_CONVERSION_TYPES = Literal["USD", "BRL", "EUR", "BTC", "ETH"]


class ConversionResponse(BaseModel):
    from_currency: str
    to_currency: str
    original_amount: float
    converted_amount: float
