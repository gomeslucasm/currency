from app.repositories.currency import ExchangeRateAPIRepository, ExchangeRateRepository
from app.schemas.conversion import ALLOWED_CONVERSION_TYPES


class ConversionService:
    ALLOWED_CURRENCIES = {"USD", "BRL", "EUR", "BTC", "ETH"}

    def __init__(self, exchange_rate_repository: ExchangeRateRepository):
        self.exchange_rate_repository = exchange_rate_repository

    def validate_currencies(
        self,
        base_currency: str,
        target_currency: str,
    ):
        if (
            base_currency not in self.ALLOWED_CURRENCIES
            or target_currency not in self.ALLOWED_CURRENCIES
        ):
            allowed_currencies = ", ".join(sorted(self.ALLOWED_CURRENCIES))
            raise ValueError(
                f"Conversion not allowed for given currencies. Allowed currencies are: {allowed_currencies}"
            )

    def __get_amount_in_usd(self, from_currency: str, amount: float) -> float:
        if from_currency == "USD":
            return amount
        exchange_rate = self.exchange_rate_repository.get_exchange_rate(
            from_currency, "USD"
        )
        return amount * exchange_rate.rate

    def __convert_from_usd(self, to_currency: str, amount_in_usd: float) -> float:
        if to_currency == "USD":
            return amount_in_usd
        exchange_rate = self.exchange_rate_repository.get_exchange_rate(
            "USD", to_currency
        )
        return amount_in_usd * exchange_rate.rate

    def convert(
        self,
        from_currency: str,
        to_currency: str,
        amount: float,
    ) -> float:
        self.validate_currencies(from_currency, to_currency)
        amount_in_usd = self.__get_amount_in_usd(from_currency, amount)
        return self.__convert_from_usd(to_currency, amount_in_usd)


def get_conversion_service() -> ConversionService:
    return ConversionService(ExchangeRateAPIRepository())
