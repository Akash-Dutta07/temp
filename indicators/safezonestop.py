from jesse.indicators.safezonestop import safezonestop
import numpy as np

def calculate_safezonestop(candles: np.ndarray, period: int, mult: float, max_lookback: int, direction: str, sequential: bool):
    values = safezonestop(
        candles=candles,
        period=period,
        mult=mult,
        max_lookback=max_lookback,
        direction=direction,
        sequential=sequential
    )

    return np.where(np.isnan(values), None, values).tolist()
    
