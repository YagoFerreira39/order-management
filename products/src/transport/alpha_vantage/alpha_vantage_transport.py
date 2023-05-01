import requests
from decouple import config

from src.core.abstract.transport_abstract import TransportAbstract
from src.domain.enums.transport.alpha_vantage.alpha_vantage_enum import AlphaVantageEnum


class AlphaVantageTransport(TransportAbstract):
    __api_url = config("ALPHA_VANTAGE_URL")
    __api_key = config("ALPHA_VANTAGE_KEY")

    @classmethod
    async def symbol_search(cls, symbol: str) -> dict:
        params = {
            "function": AlphaVantageEnum.SYMBOL_SEARCH,
            "keywords": symbol,
            "apikey": cls.__api_key
        }

        api_response = requests.get(url=cls.__api_url, params=params)
        response = api_response.json()

        return response

    @classmethod
    async def symbol_detail(cls, symbol: str) -> dict:
        params = {
            "function": "TIME_SERIES_DAILY_ADJUSTED",
            "symbol": symbol,
            "apikey": cls.__api_key,
        }

        api_response = requests.get(url=cls.__api_url, params=params)
        response = api_response.json()

        return response
