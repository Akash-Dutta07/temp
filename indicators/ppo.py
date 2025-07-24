import numpy as np
from jesse.indicators.ppo import ppo

def calculate_ppo(candles: np.ndarray, fast_period: int = 12, slow_period: int = 26) -> dict:
    ppo_values = ppo(candles, fast_period=fast_period, slow_period=slow_period, source_type="close", sequential=True)
    clean_ppo = ppo_values[~np.isnan(ppo_values)]

    return {
        "indicator": "ppo",
        "values": clean_ppo.tolist()
    }
