from jesse.indicators.hma import hma
import numpy as np

def calculate_hma(candles, period: int, source_type: str):
    values = hma(
        candles,
        period=period,
        source_type=source_type,
        sequential=True
    )

    return {
        "hma": np.where(np.isnan(values), None, values).tolist()
    }
