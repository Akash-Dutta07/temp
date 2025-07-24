import numpy as np
from jesse.indicators.bollinger_bands import bollinger_bands

def calculate_bollinger(candles: np.ndarray, period: int) -> dict:
    # remove `multiplier=` since it's not accepted
    upper, middle, lower = bollinger_bands(
        candles,
        period=period,
        source_type="close",
        sequential=True
    )

    clean_upper = upper[~np.isnan(upper)]
    clean_middle = middle[~np.isnan(middle)]
    clean_lower = lower[~np.isnan(lower)]

    return {
        "indicator": "bollinger_bands",
        "upper_band": clean_upper.tolist(),
        "middle_band": clean_middle.tolist(),
        "lower_band": clean_lower.tolist()
    }
