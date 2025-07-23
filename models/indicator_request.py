from pydantic import BaseModel

class IndicatorRequest(BaseModel):
    symbol: str     # e.g., "BTCUSDT"
    interval: str   # e.g., "5m", "1h"
    period: int     # e.g., 20
    limit: int = 100  # default number of candles
