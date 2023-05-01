from src.domain.models.symbol.symbol_model import SymbolModel


class SymbolDetailExtension:

    @staticmethod
    def to_model(response: dict) -> SymbolModel:
        meta_data = response.get("Meta Data", dict())
        symbol = meta_data.get("2. Symbol")
        last_date = meta_data.get("3. Last Refreshed")
        data = response.get("Time Series (Daily)", dict()).get(last_date, dict())
        print(data)

        model: SymbolModel = {
            "last_date": last_date,
            "symbol": symbol,
            "open": float(data.get("1. open", 0)),
            "high": float(data.get("2. high", 0)),
            "low": float(data.get("3. low", 0)),
            "close": float(data.get("4. close", 0)),
            "adjusted_close": float(data.get("5. adjusted close", 0)),
            "volume": int(data.get("6. volume", 0)),
            "dividend_amount": float(data.get("7. dividend amount", 0)),
            "split_coefficient": float(data.get("8. split coefficient", 0)),
        }

        return model
