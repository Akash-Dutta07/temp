import numpy as np
from jesse.indicators.efi import efi as jesse_efi

def calculate_efi(candles: np.ndarray, period: int, source_type: str) -> list:
    def same_length(arr, reference):
        if isinstance(arr, np.ndarray) and isinstance(reference, np.ndarray):
            if arr.shape[0] < reference.shape[0]:
                pad = np.full((reference.shape[0] - arr.shape[0],), np.nan)
                arr = np.concatenate([pad, arr])
        return arr

    def remove_nan(arr):
        return [round(float(v), 6) if not np.isnan(v) else None for v in arr]

    efi_values = jesse_efi(candles, period=period, source_type=source_type, sequential=True)
    return remove_nan(same_length(efi_values, candles))
