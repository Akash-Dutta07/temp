import numpy as np
from jesse.indicators.dm import dm as jesse_dm

def calculate_dm(candles: np.ndarray, period: int, sequential: bool):
    plus, minus = jesse_dm(
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
   


 