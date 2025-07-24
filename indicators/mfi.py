import numpy as np
from jesse.indicators.mfi import mfi

def calculate_mfi(candles: np.ndarray, period: int) -> dict:
    mfi_values = mfi(candles, period=period, sequential=True)
    clean_mfi = mfi_values[~np.isnan(mfi_values)]

    return {
        "indicator": "mfi",
        "values": clean_mfi.tolist()
    }
