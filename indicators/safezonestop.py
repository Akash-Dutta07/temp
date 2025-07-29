from jesse.indicators.safezonestop import safezonestop
import numpy as np

def calculate_safezonestop(candles, period: int, mult: float, max_lookback: int, direction: str):
    values = safezonestop(
        candles,
        period=period,
        mult=mult,
        max_lookback=max_lookback,
        direction=direction,
        sequential=True
    )

    return {
        "safezonestop": np.where(np.isnan(values), None, values).tolist()
    }
