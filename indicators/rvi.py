import numpy as np
from jesse.indicators.rvi import rvi as jesse_rvi

def calculate_rvi(candles: np.ndarray, period: int, ma_len: int, matype: int, devtype: int,
                  source_type: str, sequential: bool):
    result = jesse_rvi(
        candles=candles,
        period=period,
        ma_len=ma_len,
        matype=matype,
        devtype=devtype,
        source_type=source_type,
        sequential=sequential
    )

    if sequential:
        return [None if np.isnan(x) else float(x) for x in result]
    return float(result)
