from jesse.indicators.alligator import alligator
import numpy as np

def calculate_alligator(candles, source_type: str):
    jaw, teeth, lips = alligator(
        candles,
        source_type=source_type,
        sequential=True
    )

    return {
        "jaw": np.where(np.isnan(jaw), None, jaw).tolist(),
        "teeth": np.where(np.isnan(teeth), None, teeth).tolist(),
        "lips": np.where(np.isnan(lips), None, lips).tolist()
    }
