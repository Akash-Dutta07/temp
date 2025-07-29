from jesse.indicators.linearreg import linearreg
import numpy as np

def calculate_linearreg(candles, period: int, source_type: str):
    values = linearreg(
        candles,
        period=period,
        source_type=source_type,
        sequential=True
    )

    return {
        "linearreg": np.where(np.isnan(values), None, values).tolist()
    }
