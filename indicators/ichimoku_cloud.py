from jesse.indicators import ichimoku_cloud_seq
import numpy as np

def calculate_ichimoku_cloud(
    candles: np.ndarray,
    conversion_line_period: int,
    base_line_period: int,
    lagging_line_period: int,
    displacement: int,
    sequential: bool
):
    result = ichimoku_cloud_seq(
        candles,
        conversion_line_period=conversion_line_period,
        base_line_period=base_line_period,
        lagging_line_period=lagging_line_period,
        displacement=displacement,
        sequential=sequential
    )

    return {
        "conversion_line": [None if np.isnan(x) else float(x) for x in result.conversion_line],
        "base_line": [None if np.isnan(x) else float(x) for x in result.base_line],
        "span_a": [None if np.isnan(x) else float(x) for x in result.span_a],
        "span_b": [None if np.isnan(x) else float(x) for x in result.span_b],
        "lagging_line": [None if np.isnan(x) else float(x) for x in result.lagging_line],
        "future_span_a": [None if np.isnan(x) else float(x) for x in result.future_span_a],
        "future_span_b": [None if np.isnan(x) else float(x) for x in result.future_span_b],
    }
    