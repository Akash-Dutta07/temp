import numpy as np
from jesse.indicators.aroon import aroon as jesse_aroon

def calculate_aroon(candles: np.ndarray, period: int, sequential: bool):
    down, up = jesse_aroon(
        candles=candles,
        period=period,
        sequential=sequential
    )

    if sequential:
        return {
            "aroon_down": [None if np.isnan(x) else float(x) for x in down],
            "aroon_up": [None if np.isnan(x) else float(x) for x in up]
        }
    else:
        return {
            "aroon_down": float(down),
            "aroon_up": float(up)
        }
   









