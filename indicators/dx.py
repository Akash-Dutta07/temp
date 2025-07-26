import numpy as np
from jesse.indicators import dx
from jesse.helpers import slice_candles

def calculate_dx(
    candles: np.ndarray,
    di_length: int = 14,
    adx_smoothing: int = 14
) -> dict:
    sliced = slice_candles(candles, di_length + adx_smoothing + 50)
    dx_result = dx(
        sliced,
        di_length=di_length,
        adx_smoothing=adx_smoothing,
        sequential=True
    )

    return {
        "adx": [round(float(v), 6) if not np.isnan(v) else None for v in dx_result.adx],
        "plusDI": [round(float(v), 6) if not np.isnan(v) else None for v in dx_result.plusDI],
        "minusDI": [round(float(v), 6) if not np.isnan(v) else None for v in dx_result.minusDI],
    }
