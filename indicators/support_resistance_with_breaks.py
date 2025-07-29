import numpy as np

def support_resistance_with_breaks(candles: np.ndarray, left_bars: int = 15, right_bars: int = 15, vol_threshold: int = 20):
    highs = candles[:, 2]
    lows = candles[:, 3]
    closes = candles[:, 4]
    volumes = candles[:, 5]

    support = None
    resistance = None

    for i in range(left_bars, len(candles) - right_bars):
        is_support = True
        is_resistance = True

        for j in range(1, left_bars + 1):
            if lows[i] > lows[i - j]:
                is_support = False
            if highs[i] < highs[i - j]:
                is_resistance = False

        for j in range(1, right_bars + 1):
            if lows[i] > lows[i + j]:
                is_support = False
            if highs[i] < highs[i + j]:
                is_resistance = False

        if is_support:
            support = lows[i]
        if is_resistance:
            resistance = highs[i]

    if support is None:
        support = np.nan
    if resistance is None:
        resistance = np.nan

    latest_high = highs[-1]
    latest_low = lows[-1]
    latest_close = closes[-1]
    latest_volume = volumes[-1]

    green_break = bool(latest_high > resistance and latest_volume > vol_threshold)
    red_break = bool(latest_low < support and latest_volume > vol_threshold)

    bull_wick = bool(latest_high > resistance and latest_close < resistance)
    bear_wick = bool(latest_low < support and latest_close > support)

    return support, resistance, red_break, green_break, bear_wick, bull_wick


def calculate_support_resistance_with_breaks(candles, left_bars: int, right_bars: int, vol_threshold: int):
    support, resistance, red_break, green_break, bear_wick, bull_wick = support_resistance_with_breaks(
        candles,
        left_bars=left_bars,
        right_bars=right_bars,
        vol_threshold=vol_threshold
    )

    return {
        "support": float(support) if not np.isnan(support) else None,
        "resistance": float(resistance) if not np.isnan(resistance) else None,
        "red_break": bool(red_break),
        "green_break": bool(green_break),
        "bear_wick": bool(bear_wick),
        "bull_wick": bool(bull_wick)
    }
