import numpy as np
from jesse.indicators import stoch as jesse_stoch

def calculate_stoch(candles: np.ndarray, fastk_period: int, slowk_period: int,
                    slowk_matype: int, slowd_period: int, slowd_matype: int, sequential: bool):
    k, d = jesse_stoch(
        candles=candles,
        fastk_period=fastk_period,
        slowk_period=slowk_period,
        slowk_matype=slowk_matype,
        slowd_period=slowd_period,
        slowd_matype=slowd_matype,
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
