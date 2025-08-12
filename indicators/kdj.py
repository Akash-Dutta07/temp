from jesse.indicators.kdj import kdj
import numpy as np

def calculate_kdj(candles: np.ndarray, fastk_period: int, slowk_period: int, slowk_matype: int,
                  slowd_period: int, slowd_matype: int, sequential: bool):
    k, d, j = kdj(
        candles=candles,
        fastk_period=fastk_period,
        slowk_period=slowk_period,
        slowk_matype=slowk_matype,
        slowd_period=slowd_period,
        slowd_matype=slowd_matype,
        sequential=sequential
    )

    return {
        "k": np.where(np.isnan(k), None, k).tolist(),
        "d": np.where(np.isnan(d), None, d).tolist(),
        "j": np.where(np.isnan(j), None, j).tolist()
    }
