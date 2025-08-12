import numpy as np
from jesse.indicators.volume import volume as jesse_volume

def calculate_volume(candles: np.ndarray, period: int, sequential: bool):
    vol, ma = jesse_volume(
        candles=candles,
        period=period, 
        sequential=sequential
    )

    if sequential:
        return {
            "volume": [None if np.isnan(x) else float(x) for x in vol],
            "ma": [None if np.isnan(x) else float(x) for x in ma]
        }
    else:
        return {
            "volume": float(vol),
            "ma": float(ma)
        }
   


 