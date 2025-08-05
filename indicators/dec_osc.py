from jesse.indicators.dec_osc import dec_osc
import numpy as np

def calculate_dec_osc(candles, hp_period: int, k: float, source_type: str):
    values = dec_osc(
        candles,
        hp_period=hp_period,
        k=k,
        source_type=source_type,
        sequential=True
    )

    return np.where(np.isnan(values), None, values).tolist()
