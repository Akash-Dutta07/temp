import numpy as np
from jesse.indicators import srsi as jesse_srsi

def calculate_srsi(candles: np.ndarray, period: int, source_type: str, sequential: bool):
    k, d = jesse_srsi(
        candles=candles,
        period=period,
        source_type=source_type,
        sequential=sequential
    )

    if sequential:
        return {
            "k": [None if np.isnan(x) else float(x) for x in k],
            "d": [None if np.isnan(x) else float(x) for x in d]
        }
    else:
        return {
            "k": float(k),
            "d": float(d)
        }
