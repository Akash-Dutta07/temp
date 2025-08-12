import numpy as np
from jesse.indicators.ao import ao as jesse_ao

def calculate_ao(candles: np.ndarray, sequential: bool):
    osc, change = jesse_ao(
        candles=candles,
        sequential=sequential
    )

    if sequential:
        return {
            "osc": [None if np.isnan(x) else float(x) for x in osc],
            "change": [None if np.isnan(x) else float(x) for x in change]
        }
    else:
        return {
            "osc": float(osc),
            "change": float(change)
        }
   











   