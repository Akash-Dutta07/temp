from jesse.indicators.kvo import kvo
import numpy as np

def calculate_kvo(candles: np.ndarray, short_period: int, long_period: int, sequential: bool):
    values = kvo(
        candles=candles,
        short_period=short_period,
        long_period=long_period,
        sequential=sequential
    )

    return np.where(np.isnan(values), None, values).tolist()
    
