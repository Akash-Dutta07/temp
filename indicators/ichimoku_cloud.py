from jesse.indicators import ichimoku_cloud
import numpy as np

def calculate_ichimoku_cloud(
    candles: np.ndarray,
    conversion_line_period: int = 9,
    base_line_period: int = 26,
    lagging_line_period: int = 52,
    displacement: int = 26
):
    return ichimoku_cloud(
        candles,
        conversion_line_period=conversion_line_period,
        base_line_period=base_line_period,
        lagging_line_period=lagging_line_period,
        displacement=displacement
    )
