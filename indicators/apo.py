import numpy as np
from jesse.indicators.apo import apo

def calculate_apo(candles: np.ndarray, fast_period: int = 12, slow_period: int = 26) -> dict:
    apo_values = apo(candles, fast_period=fast_period, slow_period=slow_period, source_type="close", sequential=True)
    clean_apo = apo_values[~np.isnan(apo_values)]

    return {
        "indicator": "apo",
        "values": clean_apo.tolist()
    }
