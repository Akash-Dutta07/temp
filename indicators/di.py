import numpy as np
from jesse.indicators.di import di as jesse_di

def calculate_di(candles: np.ndarray, period: int, sequential: bool):
    plus, minus = jesse_di(
        candles=candles,
        period=period, 
        sequential=sequential
    )

    if sequential:
        return {
            "plus": [None if np.isnan(x) else float(x) for x in plus],
            "minus": [None if np.isnan(x) else float(x) for x in minus]
        }
    else:
        return {
            "plus": float(plus),
            "minus": float(minus)
        }
   


 