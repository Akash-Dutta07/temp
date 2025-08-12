import numpy as np
from jesse.indicators.ppo import ppo as jesse_ppo

def calculate_ppo(candles: np.ndarray, fast_period: int, slow_period: int, matype: int,
                  source_type: str, sequential: bool):
    result = jesse_ppo(
        candles=candles,
        fast_period=fast_period,
        slow_period=slow_period,
        matype=matype,
        source_type=source_type,
        sequential=sequential
    )

    if sequential:
        return [None if np.isnan(x) else float(x) for x in result]
    else:
        return float(result)


