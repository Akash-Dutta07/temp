import numpy as np
from jesse.indicators.bollinger_bands_width import bollinger_bands_width  as jesse_bw

def calculate_bollinger_bands_width(candles: np.ndarray, period: int, mult: float, source_type: str, sequential: bool):
    result = jesse_bw(
        candles,
        period=period,
        mult=mult,
        source_type=source_type,
        sequential=sequential
    )
    
    if sequential:
        return [None if np.isnan(x) else float(x) for x in result]
    else:
        return float(result)

  