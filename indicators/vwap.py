import numpy as np
from jesse.indicators.vwap import vwap

def calculate_vwap(candles: np.ndarray) -> dict:
    vwap_values = vwap(
        candles,
        source_type="hlc3",
        anchor="D",
        sequential=True
    )

    clean_vwap = vwap_values[~np.isnan(vwap_values)]

    return {
        "indicator": "vwap",
        "values": clean_vwap.tolist()
    }
