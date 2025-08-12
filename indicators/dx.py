import numpy as np
from jesse.indicators.dx import dx as jesse_dx

def calculate_dx(candles: np.ndarray, di_length: int, adx_smoothing: int, sequential: bool):
    adx, plusDI, minusDI = jesse_dx(
        candles=candles,
        di_length=di_length,
        adx_smoothing=adx_smoothing,
        sequential=sequential
    )

    if sequential:
        return {
            "adx": [None if np.isnan(x) else float(x) for x in adx],
            "plusDI": [None if np.isnan(x) else float(x) for x in plusDI],
            "minusDI": [None if np.isnan(x) else float(x) for x in minusDI]
        }
    else:
        return {
            "adx": float(adx),
            "plusDI": float(plusDI),
            "minusDI": float(minusDI)
        }
   


