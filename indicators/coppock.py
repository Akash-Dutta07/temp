import numpy as np
from jesse.indicators.cc import cc  

def calculate_coppock(candles: np.ndarray) -> dict:
    coppock_values = cc(candles, sequential=True)
    clean_coppock = coppock_values[~np.isnan(coppock_values)]

    return {
        "indicator": "coppock",
        "values": clean_coppock.tolist()
    }
