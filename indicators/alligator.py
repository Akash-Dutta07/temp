from jesse.indicators.alligator import alligator
import numpy as np

def calculate_alligator(candles: np.ndarray, source_type: str, sequential: bool):
    jaw, teeth, lips = alligator(
        candles,
        source_type=source_type,
        sequential=sequential
    )

    return {
        "jaw": np.where(np.isnan(jaw), None, jaw).tolist(),
        "teeth": np.where(np.isnan(teeth), None, teeth).tolist(),
        "lips": np.where(np.isnan(lips), None, lips).tolist()
    }
 