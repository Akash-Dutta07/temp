from pydantic import BaseModel

class IndicatorRequest(BaseModel):
    symbol: str     # e.g., "BTCUSDT"
    interval: str   # e.g., "5m", "1h"
    period: int     # e.g., 20
    limit: int = 100  # default number of candles
    
class NoPeriodIndicatorRequest(BaseModel):
    symbol: str          # e.g., "BTCUSDT"
    interval: str        # e.g., "1h"
    limit: int = 100     # default candle limit

class ADOSCRequest(BaseModel):
    symbol: str
    interval: str
    fast_period: int = 3
    slow_period: int = 10
    limit: int = 100

class CKSPRequest(BaseModel):
    symbol: str
    interval: str
    p: int = 10
    x: float = 1.0
    q: int = 9
    limit: int = 100

class CHOPRequest(BaseModel):
    symbol: str
    interval: str
    period: int = 14
    scalar: float = 100
    drift: int = 1
    limit: int = 100

class CorrelRequest(BaseModel):
    symbol: str
    interval: str
    period: int = 5
    limit: int = 100





