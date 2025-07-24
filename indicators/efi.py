import numpy as np
from jesse.indicators.efi import efi

def calculate_efi(candles: np.ndarray, period: int) -> dict:
    efi_values = efi(candles, period=period, sequential=True)
    clean_efi = efi_values[~np.isnan(efi_values)]

    return {
        "indicator": "efi",
        "values": clean_efi.tolist()
    }
