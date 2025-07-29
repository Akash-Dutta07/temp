from jesse.indicators.nvi import nvi
import numpy as np

def calculate_nvi(candles, source_type: str):
    values = nvi(
        candles,
        source_type=source_type,
        sequential=True
    )

    return {
        "nvi": np.where(np.isnan(values), None, values).tolist()
    }
