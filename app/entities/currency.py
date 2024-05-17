from dataclasses import dataclass


@dataclass
class ExchangeRate:
    base_currency: str
    target_currency: str
    rate: float
