import numpy as np
from jesse.indicators.donchian import donchian as jesse_dh

def calculate_donchian(candles: np.ndarray, period: int, sequential: bool):
    upper, middle, lower = jesse_dh(
        candles=candles,
        period=period,
        sequential=sequential
    )

    if sequential:
        return {
            "upper_band": [None if np.isnan(x) else float(x) for x in upper],
            "middle_band": [None if np.isnan(x) else float(x) for x in middle],
            "lower_band": [None if np.isnan(x) else float(x) for x in lower]
        }
    else:
        return {
            "upper_band": float(upper),
            "middle_band": float(middle),
            "lower_band": float(lower)
        }
  
  

