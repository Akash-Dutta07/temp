import numpy as np
from jesse.indicators.supertrend import supertrend as jesse_supertrend

def calculate_supertrend(candles: np.ndarray, period: int, factor: float, sequential: bool):
    trend, changed = jesse_supertrend(
        candles=candles,
        period=period,
        factor=factor,
        sequential=sequential
    )

    if sequential:
        return {
            "trend": [None if np.isnan(x) else float(x) for x in trend],
            "changed": [None if np.isnan(x) else int(x) for x in changed]
        }
    else:
        return {
            "trend": float(trend),
            "changed": int(changed)
        }
