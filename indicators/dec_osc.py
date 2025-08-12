from jesse.indicators.dec_osc import dec_osc
import numpy as np

def calculate_dec_osc(candles: np.ndarray, hp_period: int, k: float, source_type: str, sequential: bool):
    values = dec_osc(
        candles=candles,
        hp_period=hp_period,
        k=k,
        source_type=source_type,
        sequential=sequential
    )

    return np.where(np.isnan(values), None, values).tolist()
