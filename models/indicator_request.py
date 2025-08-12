from pydantic import BaseModel , Field
from typing import Optional, Union , List , Literal

class IndicatorRequest(BaseModel):
    symbol: str     # e.g., "BTCUSDT"
    interval: str   # e.g., "5m", "1h"
    period: int     # e.g., 20
    limit: int = 100  # default number of candles
    sequential: Optional[bool] = True

class IndicatorWithSourceRequest(BaseModel):
    symbol: str                  # e.g., "BTCUSDT"
    interval: str                # e.g., "5m", "1h"
    period: int                  # e.g., 20
    limit: int = 100             # default number of candles
    source_type: Optional[str] = "close"
    sequential: Optional[bool] = True 
   
class NoPeriodIndicatorRequest(BaseModel):
    symbol: str          # e.g., "BTCUSDT"
    interval: str        # e.g., "1h"
    limit: int = 100     # default candle limit
    sequential: Optional[bool] = True

class ADOSCRequest(BaseModel):
    symbol: str
    interval: str
    fast_period: int = 3
    slow_period: int = 10
    limit: int = 100
    sequential: Optional[bool] = True

class CKSPRequest(BaseModel):
    symbol: str
    interval: str
    p: int = 10
    x: float = 1.0
    q: int = 9
    limit: int = 100
    sequential: Optional[bool] = True

class CHOPRequest(BaseModel):
    symbol: str
    interval: str
    period: int = 14
    scalar: float = 100
    drift: int = 1
    limit: int = 100
    sequential: Optional[bool] = True

class DXRequest(BaseModel):
    symbol: str
    interval: str
    di_length: int = 14 
    adx_smoothing: int = 14
    limit: int = 100
    sequential: Optional[bool] = True

class KSTRequest(BaseModel):
    symbol: str
    interval: str
    #period: int
    limit: int = 100
    source_type: Optional[str] = "close"

    sma_period1: Optional[int] = 10
    sma_period2: Optional[int] = 10
    sma_period3: Optional[int] = 10
    sma_period4: Optional[int] = 15

    roc_period1: Optional[int] = 10
    roc_period2: Optional[int] = 15
    roc_period3: Optional[int] = 20
    roc_period4: Optional[int] = 30

    signal_period: Optional[int] = 9
    sequential: Optional[bool] = True

class APORequest(BaseModel):
    symbol: str
    interval: str
    limit: int = 100
    source_type: Optional[str] = "close"
    fast_period: Optional[int] = 12
    slow_period: Optional[int] = 26
    matype: Optional[int] = 0
    sequential: Optional[bool] = True

class BollingerBandsWidthRequest(BaseModel):
    symbol: str
    interval: str
    period: int = 20
    mult: float = 2
    source_type: str = "close"
    limit: int
    sequential: Optional[bool] = True
    

class BollingerBandsRequest(BaseModel):
    symbol: str
    interval: str
    period: int = 20
    devup: float = 2
    devdn: float = 2
    matype: int = 0
    devtype: int = 0
    source_type: str = "close"
    limit: int
    sequential: bool = True

class IchimokuCloudRequest(BaseModel):
    symbol: str
    interval: str
    conversion_line_period: int = 9
    base_line_period: int = 26
    lagging_line_period: int = 52
    displacement: int = 26
    limit: int
    sequential: Optional[bool] = True

class CFORequest(BaseModel):
    symbol: str
    interval: str
    period: Optional[int] = 14
    scalar: Optional[float] = 100
    source_type: Optional[str] = "close"
    limit: Optional[int] = 100 
    sequential: Optional[bool] = True

class CCRequest(BaseModel):
    symbol: str
    interval: str
    wma_period: int = 10
    roc_short_period: int = 11
    roc_long_period: int = 14
    limit: int = 100
    source_type: Optional[str] = "close"
    sequential: Optional[bool] = True

class IndicatorWithLengthAndDivRequest(BaseModel):
    symbol: str
    interval: str
    limit: int
    length: int = 14
    div: int = 10000
    sequential: Optional[bool] = True

class KeltnerRequest(BaseModel):
    symbol: str
    interval: str
    limit: int
    period: int = 20
    multiplier: float = 2 
    matype: int = 1
    source_type: Literal["open", "high", "low", "close"] = "close"
    sequential: bool = True

class MACDRequest(BaseModel):
    symbol: str
    interval: str
    limit: int
    fast_period: int = 12
    slow_period: int = 26
    signal_period: int = 9
    source_type: Literal["close", "open", "high", "low"] = "close"
    sequential: bool = True

class PPORequest(BaseModel):
    symbol: str = Field(..., example="BTCUSDT")
    interval: str = Field(..., example="1h")
    limit: int = Field(100, example=100)
    fast_period: int = Field(12, example=12)
    slow_period: int = Field(26, example=26)
    matype: int = Field(0, example=0)
    source_type: Literal["close", "open", "high", "low"] = Field("close", example="close")
    sequential: bool = Field(True, example=True)

class SupertrendRequest(BaseModel):
    symbol: str = Field(..., example="BTCUSDT")
    interval: str = Field(..., example="1h")
    limit: int = Field(100, example=100)
    period: int = Field(10, example=10)
    factor: float = Field(3, example=3)
    sequential: bool = Field(True, example=True)

class VWAPRequest(BaseModel):
    symbol: str = Field(..., example="BTCUSDT")
    interval: str = Field(..., example="1h")
    limit: int = Field(100, example=100)
    source_type: Literal["open", "high", "low", "close", "hl2", "hlc3", "ohlc4"] = Field("hlc3", example="hlc3")
    anchor: Literal["Y", "M", "W", "D", "h", "m"] = Field("D", example="D")
    sequential: bool = Field(True, example=True)

class McGinleyRequest(BaseModel):
    symbol: str = Field(..., example="BTCUSDT")
    interval: str = Field(..., example="1h")
    limit: int = Field(100, example=100)
    period: int = Field(10, example=10)
    k: float = Field(0.6, example=0.6)
    source_type: Literal["open", "high", "low", "close"] = Field("close", example="close")
    sequential: bool = Field(True, example=True)

class MARequest(BaseModel):
    symbol: str = Field(..., example="BTCUSDT")
    interval: str = Field(..., example="1h")
    limit: int = Field(100, example=100)
    period: int = Field(30, example=30)
    matype: int = Field(0, example=0)  # e.g., 0 for SMA, 1 for EMA, etc.
    source_type: Literal["open", "high", "low", "close"] = Field("close", example="close")
    sequential: bool = Field(True, example=True)

class SARRequest(BaseModel):
    symbol: str = Field(..., example="BTCUSDT")
    interval: str = Field(..., example="1h")
    limit: int = Field(100, example=100)
    acceleration: float = Field(0.02, example=0.02)
    maximum: float = Field(0.2, example=0.2)
    sequential: bool = Field(True, example=True)

class PivotRequest(BaseModel):
    symbol: str = Field(..., example="BTCUSDT")
    interval: str = Field(..., example="1h")
    limit: int = Field(100, example=100)
    mode: int = Field(0, example=0, ge=0, le=4)
    sequential: bool = Field(True, example=True)

class ULTOSCRequest(BaseModel):
    symbol: str = Field(..., example="BTCUSDT")
    interval: str = Field(..., example="1h")
    limit: int = Field(100, example=100)
    timeperiod1: int = Field(7, example=7)
    timeperiod2: int = Field(14, example=14)
    timeperiod3: int = Field(28, example=28)
    sequential: bool = Field(True, example=True)

class VPTRequest(BaseModel):
    symbol: str = Field(..., example="BTCUSDT")
    interval: str = Field(..., example="1h")
    limit: int = Field(100, example=100)
    source_type: Literal["open", "high", "low", "close"] = Field("close", example="close")
    sequential: bool = Field(True, example=True)

class RVIRequest(BaseModel):
    symbol: str = Field(..., example="BTCUSDT")
    interval: str = Field(..., example="1h")
    limit: int = Field(100, example=100)
    period: int = Field(10, example=10)
    ma_len: int = Field(14, example=14)
    matype: int = Field(1, example=1)
    devtype: int = Field(0, example=0)
    source_type: Literal["open", "high", "low", "close"] = Field("close", example="close")
    sequential: bool = Field(True, example=True)

class StochRequest(BaseModel):
    symbol: str = Field(..., example="BTCUSDT")
    interval: str = Field(..., example="1h")
    limit: int = Field(100, example=100)
    fastk_period: int = Field(14, example=14)
    slowk_period: int = Field(3, example=3)
    slowk_matype: int = Field(0, example=0)
    slowd_period: int = Field(3, example=3)
    slowd_matype: int = Field(0, example=0)
    sequential: bool = Field(True, example=True)

class TSIRequest(BaseModel):
    symbol: str            # e.g., "BTCUSDT"
    interval: str          # e.g., "5m", "1h"
    long_period: int = 25
    short_period: int = 13
    source_type: str = "close"
    limit: int
    sequential: Optional[bool] = True

class VPWMARequest(BaseModel):
    symbol: str              # e.g., "BTCUSDT"
    interval: str            # e.g., "1h"
    period: int = 14
    power: float = 0.382
    source_type: str = "close"
    limit: int = 100         # default candle limit
    sequential: Optional[bool] = True


class SourceOnlyRequest(BaseModel):
    symbol: str                # e.g., "BTCUSDT"
    interval: str              # e.g., "1h"
    limit: int = 100           # default candle limit
    source_type: Optional[str] = "close"
    sequential: Optional[bool] = True

class ALMARequest(BaseModel):
    symbol: str                      # e.g., "BTCUSDT"
    interval: str                    # e.g., "1h"
    period: int = 9
    sigma: float = 6.0
    distribution_offset: float = 0.85
    source_type: Optional[str] = "close"
    limit: int = 100
    sequential: Optional[bool] = True


class BetaRequest(BaseModel):
    symbol: str                     # e.g., "ETHUSDT"
    benchmark_symbol: str           # e.g., "BTCUSDT"
    interval: str                   # e.g., "1h"
    period: int = 5
    limit: int = 100
    sequential: Optional[bool] = True


class KDJRequest(BaseModel):
    symbol: str = Field(..., example="BTCUSDT")
    interval: str = Field(..., example="1h")
    limit: int = Field(100, example=100)
    fastk_period: int = Field(9, example=9)
    slowk_period: int = Field(3, example=3)
    slowk_matype: Literal[0, 1, 2, 3, 4, 5] = Field(0, example=0)
    slowd_period: int = Field(3, example=3)
    slowd_matype: Literal[0, 1, 2, 3, 4, 5] = Field(0, example=0)
    sequential: bool = Field(True, example=True)


class KVORequest(BaseModel):
    symbol: str = Field(..., example="BTCUSDT")
    interval: str = Field(..., example="1h")
    limit: int = Field(100, example=100)
    short_period: int = Field(34, example=34)
    long_period: int = Field(55, example=55)
    sequential: bool = Field(True, example=True)


class MWDXRequest(BaseModel):
    symbol: str = Field(..., example="BTCUSDT")
    interval: str = Field(..., example="1h")
    limit: int = Field(100, example=100)
    factor: float = Field(0.2, example=0.2)
    source_type: Optional[str] = "close"
    sequential: bool = Field(True, example=True)


class NVIRequest(BaseModel):
    symbol: str = Field(..., example="BTCUSDT")
    interval: str = Field(..., example="1h")
    limit: int = Field(100, example=100)
    source_type: Optional[str] = "close"
    sequential: bool = Field(True, example=True)


class PVIRequest(BaseModel):
    symbol: str = Field(..., example="BTCUSDT")
    interval: str = Field(..., example="1h")
    limit: int = Field(100, example=100)
    source_type: Optional[str] = "close"
    sequential: bool = Field(True, example=True)


class DecOscRequest(BaseModel):
    symbol: str = Field(..., example="BTCUSDT")
    interval: str = Field(..., example="1h")
    limit: int = Field(100, example=100)
    hp_period: int = Field(125, example=125)
    k: float = Field(1.0, example=1.0)
    source_type: Optional[str] = "close"
    sequential: bool = Field(True, example=True)


class SafeZoneStopRequest(BaseModel):
    symbol: str = Field(..., example="BTCUSDT")
    interval: str = Field(..., example="1h")
    limit: int = Field(100, example=100)
    period: int = Field(22, example=22)
    mult: float = Field(2.5, example=2.5)
    max_lookback: int = Field(3, example=3)
    direction: Literal["long", "short"] = Field("long", example="long")
    sequential: bool = Field(True, example=True)


class SupportResistanceBreaksRequest(BaseModel):
    symbol: str = Field(..., example="BTCUSDT")
    interval: str = Field(..., example="1h")
    limit: int = Field(100, example=100)
    left_bars: int = Field(15, example=15)
    right_bars: int = Field(15, example=15)
    vol_threshold: int = Field(20, example=20)


class TTMSqueezeRequest(BaseModel):
    symbol: str
    interval: str
    length_ttms: int = 20
    bb_mult_ttms: float = 2.0
    kc_mult_low_ttms: float = 2.0
    limit: int = 100
 
 
class WTRequest(BaseModel):
    symbol: str          # e.g., "BTCUSDT"
    interval: str        # e.g., "1h"
    limit: int = 100     # number of candles
    wtchannellen: int = 9
    wtaveragelen: int = 12
    wtmalen: int = 3
    oblevel: int = 53
    oslevel: int = -53
    source_type: Optional[str] = "hlc3"
    sequential: Optional[bool] = True


class Volume24hRequest(BaseModel):
    symbol: str
    interval: str
    limit: int = 100
    candles_per_day: int = 24
    ma_period: Optional[int] = None  # e.g., 5-period MA of the 24h volumes





















