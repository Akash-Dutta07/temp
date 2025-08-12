import numpy as np
from jesse.indicators.fisher import fisher as jesse_fisher

def calculate_fisher(candles: np.ndarray, period: int, sequential: bool):
    fisher, signal = jesse_fisher(
        candles=candles,
        period=period, 
        sequential=sequential
    )

    if sequential:
        return {
            "fisher": [None if np.isnan(x) else float(x) for x in fisher],
            "signal": [None if np.isnan(x) else float(x) for x in signal]
        }
    else:
        return {
            "fisher": float(fisher),
            "signal": float(signal)
        }
   


 