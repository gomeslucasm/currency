from abc import ABC, abstractmethod
from app.entities.currency import ExchangeRate
import requests


class ExchangeRateRepository(ABC):
    @abstractmethod
    def get_exchange_rate(
        self,
        base_currency: str,
        target_currency: str,
    ) -> ExchangeRate:
        raise NotImplementedError()


class ExchangeRateAPIRepository(ExchangeRateRepository):
    def get_exchange_rate(
        self,
        base_currency: str,
        target_currency: str,
    ) -> ExchangeRate:
        response = requests.get(
            f"https://api.exchangerate-api.com/v4/latest/{base_currency}", timeout=1
        )
        if response.status_code != 200:
            raise Exception("Error fetching exchange rates")
        data = response.json()
        rate = data.get("rates", {}).get(target_currency)
        if rate is None:
            raise ValueError(f"No exchange rate found for {target_currency}")
        return ExchangeRate(
            base_currency=base_currency, target_currency=target_currency, rate=rate
        )
