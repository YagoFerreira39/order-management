from typing import Callable

from requests import Response


class TransportAbstract:
    @staticmethod
    async def __execute(callback: Callable, **kwargs) -> Response:
        response = callback(**kwargs)

        return response

    @staticmethod
    async def process_request(callback: Callable, **kwargs) -> dict:
        try:
            response = await callback(**kwargs)

            # result = response.json()

            return response

        except Exception as exception:
            raise exception
