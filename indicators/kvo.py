from jesse.indicators.kvo import kvo
import numpy as np

def calculate_kvo(candles, short_period: int, long_period: int):
    values = kvo(
        candles,
        short_period=short_period,
        long_period=long_period,
        sequential=True
    )

    return {
        "kvo": np.where(np.isnan(values), None, values).tolist()
    }
