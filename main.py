from fastapi import FastAPI, HTTPException

from models.indicator_request import IndicatorRequest
from models.indicator_request import NoPeriodIndicatorRequest
from models.indicator_request import ADOSCRequest
from models.indicator_request import CKSPRequest
from models.indicator_request import CHOPRequest
from models.indicator_request import DXRequest
from models.indicator_request import IndicatorWithSourceRequest
from models.indicator_request import KSTRequest
from models.indicator_request import APORequest
from models.indicator_request import BollingerBandsWidthRequest
from models.indicator_request import BollingerBandsRequest
from models.indicator_request import IchimokuCloudRequest
from models.indicator_request import CFORequest
from models.indicator_request import CCRequest
from models.indicator_request import IndicatorWithLengthAndDivRequest
from models.indicator_request import KeltnerRequest
from models.indicator_request import MACDRequest
from models.indicator_request import PPORequest
from models.indicator_request import SupertrendRequest
from models.indicator_request import VWAPRequest
from models.indicator_request import McGinleyRequest
from models.indicator_request import MARequest
from models.indicator_request import SARRequest
from models.indicator_request import PivotRequest
from models.indicator_request import ULTOSCRequest
from models.indicator_request import VPTRequest
from models.indicator_request import RVIRequest
from models.indicator_request import StochRequest
from models.indicator_request import TSIRequest
from models.indicator_request import VPWMARequest

from services.binance_service import fetch_candles

from indicators.sma import calculate_sma
from indicators.rsi import calculate_rsi
from indicators.ema import calculate_ema
from indicators.macd import calculate_macd
from indicators.bollinger_bands import calculate_bollinger_bands
from indicators.atr import calculate_atr
from indicators.supertrend import calculate_supertrend
from indicators.vwap import calculate_vwap
from indicators.adx import calculate_adx
from indicators.cci import calculate_cci
from indicators.williams import calculate_williams_r
from indicators.roc import calculate_roc
from indicators.cmo import calculate_cmo
from indicators.apo import calculate_apo
from indicators.ppo import calculate_ppo
from indicators.mfi import calculate_mfi
from indicators.cc import calculate_cc
from indicators.donchian import calculate_donchian
from indicators.obv import calculate_obv
from indicators.efi import calculate_efi
from indicators.cksp import calculate_cksp
from indicators.chop import chop
from indicators.correl import calculate_correl
from indicators.dpo import calculate_dpo
from indicators.dm import calculate_dm
from indicators.aroon import calculate_aroon
from indicators.ao import calculate_ao
from indicators.bop import calculate_bop
from indicators.ad import ad
from indicators.bollinger_bands_width import calculate_bollinger_bands_width
from indicators.cfo import calculate_cfo
from indicators.adosc import adosc
from indicators.dx import calculate_dx
from indicators.dema import dema
from indicators.calculate_fisher import calculate_fisher
from indicators.ichimoku_cloud import calculate_ichimoku_cloud
from indicators.di import calculate_di
from indicators.emv import calculate_emv
from indicators.keltner import calculate_keltner
from indicators.kst import calculate_kst
from indicators.mass import calculate_mass
from indicators.apo import calculate_apo
from indicators.cfo import calculate_cfo
from indicators.mcginley_dynamic import calculate_mcginley
from indicators.ma import calculate_ma
from indicators.mean_ad import calculate_mean_ad
from indicators.median_ad import calculate_median_ad
from indicators.medprice import calculate_medprice
from indicators.mom import calculate_mom
from indicators.wma import calculate_wma
from indicators.sar import calculate_sar
from indicators.pivot import calculate_pivot
from indicators.ultosc import calculate_ultosc
from indicators.vpt import calculate_vpt
from indicators.rocp import calculate_rocp
from indicators.rocr import calculate_rocr
from indicators.rocr100 import calculate_rocr100
from indicators.rvi import calculate_rvi
from indicators.smma import calculate_smma
from indicators.stoch import calculate_stoch
from indicators.tsi import calculate_tsi
from indicators.ttm_trend import calculate_ttm_trend
from indicators.tema import calculate_tema
from indicators.trix import calculate_trix
from indicators.volume import calculate_volume
from indicators.vpwma import calculate_vpwma
from indicators.vwma import calculate_vwma

import numpy as np
from fastapi.responses import JSONResponse

app = FastAPI()

# Simple Moving Average (SMA)
@app.post("/sma")
async def get_sma(data: IndicatorWithSourceRequest):
    candles = await fetch_candles(data.symbol, data.interval, data.limit)
    values = calculate_sma(
        candles=candles,
        period=data.period,
        source_type=data.source_type,
        sequential=True  # always array output
    )

    return {
        "indicator": "sma",
        "symbol": data.symbol.upper(),
        "interval": data.interval,
        "period": data.period,
        "source_type": data.source_type,
        "values": values
    }

# Relative Strength Index (RSI)
@app.post("/rsi")
async def get_rsi(data: IndicatorWithSourceRequest):
    candles = await fetch_candles(data.symbol, data.interval, data.limit)
    values = calculate_rsi(
        candles=candles,
        period=data.period,
        source_type=data.source_type,
        sequential=True  # array output
    )

    return {
        "indicator": "rsi",
        "symbol": data.symbol.upper(),
        "interval": data.interval,
        "period": data.period,
        "source_type": data.source_type,
        "values": values
    }

# EMA -Exponential Moving Average
@app.post("/ema")
async def get_ema(data: IndicatorWithSourceRequest):
    candles = await fetch_candles(data.symbol, data.interval, data.limit)
    result = calculate_ema(candles, data.period, data.source_type, sequential=True)
    
    return {
        "indicator": "ema",
        "symbol": data.symbol.upper(),
        "interval": data.interval,
        "period": data.period,
        "source_type": data.source_type,
        "values": result
    }

# Moving Average Convergence Divergence (MACD)
@app.post("/macd")
async def get_macd(data: MACDRequest):
    candles = await fetch_candles(data.symbol, data.interval, data.limit)
    result = calculate_macd(
        candles=candles,
        fast_period=data.fast_period,
        slow_period=data.slow_period,
        signal_period=data.signal_period,
        source_type=data.source_type,
        sequential=data.sequential
    )
    return {
        "indicator": "macd",
        "symbol": data.symbol.upper(),
        "interval": data.interval,
        "fast_period": data.fast_period,
        "slow_period": data.slow_period,
        "signal_period": data.signal_period,
        "values": result
    }

# Bollinger Bands
@app.post("/bollinger-bands")
async def get_bollinger_bands(data: BollingerBandsRequest):
    candles = await fetch_candles(data.symbol, data.interval, data.limit)

    result = calculate_bollinger_bands(
        candles,
        period=data.period,
        devup=data.devup,
        devdn=data.devdn,
        matype=data.matype,
        devtype=data.devtype,
        source_type=data.source_type,
        sequential=data.sequential
    )

    return {
        "indicator": "bollinger_bands",
        "symbol": data.symbol.upper(),
        "interval": data.interval,
        "period": data.period,
        "values": result
    }

#Average True Range (ATR)
@app.post("/atr")
async def get_atr(data: IndicatorRequest):
    try:
        candles = await fetch_candles(data.symbol, data.interval, data.limit)
        result = calculate_atr(candles, data.period)
        result.update({
            "symbol": data.symbol.upper(),
            "interval": data.interval,
            "period": data.period
        })
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# SuperTrend
@app.post("/supertrend")
async def get_supertrend(data: SupertrendRequest):
    candles = await fetch_candles(data.symbol, data.interval, data.limit)
    values = calculate_supertrend(
        candles=candles,
        period=data.period,
        factor=data.factor,
        sequential=data.sequential
    )

    return {
        "indicator": "supertrend",
        "symbol": data.symbol.upper(),
        "interval": data.interval,
        "period": data.period,
        "factor": data.factor,
        "values": values
    }
    
# Volume Weighted Average Price (VWAP)
@app.post("/vwap")
async def get_vwap(data: VWAPRequest):
    candles = await fetch_candles(data.symbol, data.interval, data.limit)
    values = calculate_vwap(
        candles=candles,
        source_type=data.source_type,
        anchor=data.anchor,
        sequential=data.sequential
    )

    return {
        "indicator": "vwap",
        "symbol": data.symbol.upper(),
        "interval": data.interval,
        "source_type": data.source_type,
        "anchor": data.anchor,
        "values": values
    }

# Average Directional Movement Index (ADX)
@app.post("/adx")
async def get_adx(data: IndicatorRequest):
    try:
        candles = await fetch_candles(data.symbol, data.interval, data.limit)
        result = calculate_adx(candles, data.period)
        result.update({
            "symbol": data.symbol.upper(),
            "interval": data.interval,
            "period": data.period
        })
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Commodity Channel Index (CCI)
@app.post("/cci")
async def get_cci(data: IndicatorRequest):
    try:
        candles = await fetch_candles(data.symbol, data.interval, data.limit)
        result = calculate_cci(candles, data.period)
        result.update({
            "symbol": data.symbol.upper(),
            "interval": data.interval,
            "period": data.period
        })
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Williams' %R(willr)
@app.post("/williams_r")
async def get_williams_r(data: IndicatorRequest):
    try:
        candles = await fetch_candles(data.symbol, data.interval, data.limit)
        result = calculate_williams_r(candles, data.period)
        return result
    except Exception as e:
        return JSONResponse(status_code=500, content={"detail": str(e)})    

#  Rate of Change (ROC)
@app.post("/roc")
async def get_roc(data: IndicatorWithSourceRequest):
    candles = await fetch_candles(data.symbol, data.interval, data.limit)
    values = calculate_roc(
        candles=candles,
        period=data.period,
        source_type=data.source_type,
        sequential=True  # return array
    )

    return {
        "indicator": "roc",
        "symbol": data.symbol.upper(),
        "interval": data.interval,
        "period": data.period,
        "source_type": data.source_type,
        "values": values
    }

#  Chande Momentum Oscillator (CMO)
@app.post("/cmo")
async def get_cmo(data: IndicatorWithSourceRequest):
    candles = await fetch_candles(data.symbol, data.interval, data.limit)
    values = calculate_cmo(
        candles,
        period=data.period,
        source_type=data.source_type
    )

    cleaned_values = [round(float(v), 4) if not np.isnan(v) else None for v in values]

    return {
        "indicator": "cmo",
        "symbol": data.symbol.upper(),
        "interval": data.interval,
        "period": data.period,
        "values": cleaned_values
    }

# Absolute Price Oscillator (APO)
@app.post("/apo")
async def get_apo(data: APORequest):
    candles = await fetch_candles(data.symbol, data.interval, data.limit)

    result = calculate_apo(
        candles=candles,
        fast_period=data.fast_period,
        slow_period=data.slow_period,
        matype=data.matype,
        source_type=data.source_type,
        sequential=True
    )

    return {
        "indicator": "apo",
        "symbol": data.symbol.upper(),
        "interval": data.interval,
        "fast_period": data.fast_period,
        "slow_period": data.slow_period,
        "matype": data.matype,
        "source_type": data.source_type,
        "sequential": True,
        "values": result
    }

# Percentage Price Oscillator (PPO)
@app.post("/ppo")
async def get_ppo(data: PPORequest):
    candles = await fetch_candles(data.symbol, data.interval, data.limit)
    values = calculate_ppo(
        candles=candles,
        fast_period=data.fast_period,
        slow_period=data.slow_period,
        matype=data.matype,
        source_type=data.source_type,
        sequential=data.sequential
    )

    return {
        "indicator": "ppo",
        "symbol": data.symbol.upper(),
        "interval": data.interval,
        "fast_period": data.fast_period,
        "slow_period": data.slow_period,
        "matype": data.matype,
        "source_type": data.source_type,
        "values": values
    }

# Money Flow Index (MFI)
@app.post("/mfi")
async def get_mfi(data: IndicatorRequest):
    candles = await fetch_candles(data.symbol, data.interval, data.limit)
    values = calculate_mfi(candles, data.period, sequential=True)

    return {
        "indicator": "mfi",
        "symbol": data.symbol.upper(),
        "interval": data.interval,
        "period": data.period,
        "values": values
    }

# Coppock Curve (CC)
@app.post("/cc")
async def get_cc(data: CCRequest):
    candles = await fetch_candles(data.symbol, data.interval, data.limit)
    values = calculate_cc(
        candles,
        wma_period=data.wma_period,
        roc_short_period=data.roc_short_period,
        roc_long_period=data.roc_long_period,
        source_type=data.source_type
    )

    cleaned_values = [round(float(v), 4) if not np.isnan(v) else None for v in values]

    return {
        "indicator": "cc",
        "symbol": data.symbol.upper(),
        "interval": data.interval,
        "wma_period": data.wma_period,
        "roc_short_period": data.roc_short_period,
        "roc_long_period": data.roc_long_period,
        "values": cleaned_values
    }

# Donchian Channels (donchian)
@app.post("/donchian")
async def get_donchian(data: IndicatorRequest):
    try:
        candles = await fetch_candles(data.symbol, data.interval, data.limit)
        result = calculate_donchian(candles, period=data.period)
        return result
    except Exception as e:
        return JSONResponse(status_code=500, content={"detail": str(e)})

# On Balance Volume (OBV)
@app.post("/obv")
async def get_obv(data: NoPeriodIndicatorRequest):
    candles = await fetch_candles(data.symbol, data.interval, data.limit)
    values = calculate_obv(candles, sequential=True)

    return {
        "indicator": "obv",
        "symbol": data.symbol.upper(),
        "interval": data.interval,
        "values": values
    }

# Elder's Force Index (EFI)
@app.post("/efi")
async def get_efi(data: IndicatorWithSourceRequest):
    candles = await fetch_candles(data.symbol, data.interval, data.limit)
    efi_values = calculate_efi(candles, data.period, data.source_type)

    return {
        "indicator": "efi",
        "symbol": data.symbol.upper(),
        "interval": data.interval,
        "period": data.period,
        "source_type": data.source_type,
        "values": efi_values
    }

# Aroon indicator
@app.post("/aroon")
async def get_aroon(data: IndicatorRequest):
    """ aroon - Aroon indicator"""
    candles = await fetch_candles(data.symbol, data.interval, data.limit)
    result = calculate_aroon(candles, data.period)

    return {
        "indicator": "aroon",
        "symbol": data.symbol.upper(),
        "interval": data.interval,
        "period": data.period,
        "values": result
    }

# Awesome Oscillator (ao)
@app.post("/ao")
async def get_ao(data: NoPeriodIndicatorRequest):
    """Ao -Awesome Oscillator"""
    candles = await fetch_candles(data.symbol, data.interval, data.limit)
    ao_values = calculate_ao(candles, sequential=True)

    return {
        "indicator": "ao",
        "symbol": data.symbol.upper(),
        "interval": data.interval,
        "values": ao_values
    }

# Balance of Power (BOP)
@app.post("/bop")
async def get_bop(data: NoPeriodIndicatorRequest):
    """BOP - Balance of Power"""
    candles = await fetch_candles(data.symbol, data.interval, data.limit)
    bop_values = calculate_bop(candles, sequential=True)

    return {
        "indicator": "bop",
        "symbol": data.symbol.upper(),
        "interval": data.interval,
        "values": bop_values
    }

# Accumulation/Distribution Line (AD)
@app.post("/ad")
async def get_ad_handler(data: NoPeriodIndicatorRequest):
    """AD - Accumulation/Distribution Line"""
    candles = await fetch_candles(data.symbol, data.interval, data.limit)
    result = ad(candles, sequential=True)
    return {
        "indicator": "ad",
        "symbol": data.symbol.upper(),
        "interval": data.interval,
        "values": result.tolist() if hasattr(result, "tolist") else result
    }


# Bollinger Bands Width
@app.post("/bollinger-bands-width")
async def get_bollinger_bands_width(data: BollingerBandsWidthRequest):
    candles = await fetch_candles(data.symbol, data.interval, data.limit)
    raw_values = calculate_bollinger_bands_width(
        candles,
        period=data.period,
        mult=data.mult,
        source_type=data.source_type
    )

    # Replace NaNs with None so FastAPI can return them properly
    cleaned_values = [float(v) if not np.isnan(v) else None for v in raw_values]

    return {
        "indicator": "bollinger_bands_width",
        "symbol": data.symbol.upper(),
        "interval": data.interval,
        "period": data.period,
        "mult": data.mult,
        "source_type": data.source_type,
        "values": cleaned_values
    }

# Chande Forecast Oscillator (CFO)   
@app.post("/cfo")
async def get_cfo(data: CFORequest):
    candles = await fetch_candles(data.symbol, data.interval, data.limit)
    result = calculate_cfo(candles, data.period, data.scalar, data.source_type)

    # Clean NaNs for JSON
    import numpy as np
    result_cleaned = [round(x, 5) if not np.isnan(x) else None for x in result]

    return {
        "indicator": "cfo",
        "symbol": data.symbol.upper(),
        "interval": data.interval,
        "period": data.period,
        "scalar": data.scalar,
        "values": result_cleaned
    }

# Chaikin A/D Oscillator(adosc)
@app.post("/adosc")
async def get_adosc(data: ADOSCRequest):
    """ADOSC - Chaikin Oscillator"""
    candles = await fetch_candles(data.symbol, data.interval, data.limit)
    result = adosc(candles, data.fast_period, data.slow_period, sequential=True)
    return {
        "indicator": "adosc",
        "symbol": data.symbol.upper(),
        "interval": data.interval,
        "fast_period": data.fast_period,
        "slow_period": data.slow_period,
        "values": result.tolist() if hasattr(result, "tolist") else result
    }


# Chande Kroll Stop (CKSP)
@app.post("/cksp")
async def get_cksp(data: CKSPRequest):
    candles = await fetch_candles(data.symbol, data.interval, data.limit)
    result = calculate_cksp(
        candles,
        p=data.p,
        x=data.x,
        q=data.q
    )

    def safe_array(arr):
        return [None if isinstance(x, float) and (np.isnan(x) or np.isinf(x)) else x for x in arr.tolist()]

    return {
        "indicator": "cksp",
        "symbol": data.symbol.upper(),
        "interval": data.interval,
        "long": safe_array(result.long),
        "short": safe_array(result.short)
    }



# Choppiness Index (CHOP)
@app.post("/chop")
async def get_chop(data: CHOPRequest):
    candles = await fetch_candles(data.symbol, data.interval, data.limit)

    result = chop(
        candles,
        period=data.period,
        scalar=data.scalar,
        drift=data.drift,
        sequential=True
    )

    # Convert NaN to None for safe JSON response
    clean_result = [None if np.isnan(x) else x for x in result]

    return {
        "indicator": "chop",
        "symbol": data.symbol.upper(),
        "interval": data.interval,
        "period": data.period,
        "scalar": data.scalar,
        "drift": data.drift,
        "values": clean_result
    }


# Pearson's Correlation Coefficient
@app.post("/correl")
async def get_correl(data: IndicatorRequest):
    candles = await fetch_candles(data.symbol, data.interval, data.limit)
    result = calculate_correl(candles, data.period)
    values = [round(float(v), 6) if not np.isnan(v) else None for v in result]

    return {
        "symbol": data.symbol.upper(),
        "interval": data.interval,
        "period": data.period,
        "values": values
    }


# Detrended Price Oscillator (DPO)
@app.post("/dpo")
async def get_dpo(data: IndicatorWithSourceRequest):
    candles = await fetch_candles(data.symbol, data.interval, data.limit)
    dpo_values = calculate_dpo(candles, data.period, data.source_type)

    return {
        "indicator": "dpo",
        "symbol": data.symbol.upper(),
        "interval": data.interval,
        "period": data.period,
        "source_type": data.source_type,
        "values": dpo_values
    }



# Directional Movement (dm)
@app.post("/dm")
async def get_dm(data: IndicatorRequest):
    candles = await fetch_candles(data.symbol, data.interval, data.limit)
    dm_values = calculate_dm(candles, data.period)

    return {
        "indicator": "dm",
        "symbol": data.symbol.upper(),
        "interval": data.interval,
        "period": data.period,
        "plus": dm_values["plus"],
        "minus": dm_values["minus"]
    }


#  Directional Movement Index (DMI) 
@app.post("/dx")
async def get_dx(data: DXRequest):
    candles = await fetch_candles(data.symbol, data.interval, data.limit)
    dx_values = calculate_dx(candles, data.di_length, data.adx_smoothing)

    return {
        "indicator": "dx",
        "symbol": data.symbol.upper(),
        "interval": data.interval,
        "di_length": data.di_length,
        "adx_smoothing": data.adx_smoothing,
        "adx": dx_values["adx"],
        "plusDI": dx_values["plusDI"],
        "minusDI": dx_values["minusDI"]
    }



# Double Exponential Moving Average (DEMA)
@app.post("/dema")
async def get_dema(data: IndicatorWithSourceRequest):
    candles = await fetch_candles(data.symbol, data.interval, data.limit)
    dema_values = dema(candles, data.period, data.source_type, sequential=True)

    return {
        "indicator": "dema",
        "symbol": data.symbol.upper(),
        "interval": data.interval,
        "period": data.period,
        "source_type": data.source_type,
        "values": dema_values.tolist()
    }



#  Fisher Transform (fisher)
@app.post("/fisher")
async def get_fisher(data: IndicatorRequest):
    candles = await fetch_candles(data.symbol, data.interval, data.limit)
    fisher_values = calculate_fisher(candles, data.period)
    return {
        "indicator": "fisher",
        "symbol": data.symbol.upper(),
        "interval": data.interval,
        "period": data.period,
        "values": fisher_values
    }


# ichimoku_cloud
@app.post("/ichimoku-cloud")
async def get_ichimoku_cloud(data: IchimokuCloudRequest):
    candles = await fetch_candles(data.symbol, data.interval, data.limit)
    result = calculate_ichimoku_cloud(
        candles,
        conversion_line_period=data.conversion_line_period,
        base_line_period=data.base_line_period,
        lagging_line_period=data.lagging_line_period,
        displacement=data.displacement
    )

    return {
        "indicator": "ichimoku_cloud",
        "symbol": data.symbol.upper(),
        "interval": data.interval,
        "conversion_line": result.conversion_line.tolist() if hasattr(result.conversion_line, "tolist") else result.conversion_line,
        "base_line": result.base_line.tolist() if hasattr(result.base_line, "tolist") else result.base_line,
        "span_a": result.span_a.tolist() if hasattr(result.span_a, "tolist") else result.span_a,
        "span_b": result.span_b.tolist() if hasattr(result.span_b, "tolist") else result.span_b,
    }



# Directional Indicator (di)
@app.post("/di")
async def get_di(data: IndicatorRequest):
    candles = await fetch_candles(data.symbol, data.interval, data.limit)
    di_values = calculate_di(candles, data.period)

    return {
        "indicator": "di",
        "symbol": data.symbol.upper(),
        "interval": data.interval,
        "period": data.period,
        "plus": di_values["plus"],
        "minus": di_values["minus"]
    }



#Ease of Movement (emv)
@app.post("/emv")
async def get_emv(data: IndicatorWithLengthAndDivRequest):
    candles = await fetch_candles(data.symbol, data.interval, data.limit)
    emv_values = calculate_emv(candles, data.length, data.div)
    
    return {
        "indicator": "emv",
        "symbol": data.symbol.upper(),
        "interval": data.interval,
        "length": data.length,
        "div": data.div,
        "values": emv_values
    }



# Keltner Channels
@app.post("/keltner")
async def get_keltner(data: KeltnerRequest):
    candles = await fetch_candles(data.symbol, data.interval, data.limit)

    keltner_values = calculate_keltner(
        candles,
        period=data.period,
        multiplier=data.multiplier,
        matype=data.matype,
        source_type=data.source_type,
        sequential=data.sequential
    )

    return {
        "indicator": "keltner",
        "symbol": data.symbol,
        "interval": data.interval,
        "period": data.period,
        "multiplier": data.multiplier,
        "matype": data.matype,
        "values": keltner_values
    }



# KST (Know Sure Thing)
@app.post("/kst")
async def get_kst(data: KSTRequest):
    candles = await fetch_candles(data.symbol, data.interval, data.limit)

    result = calculate_kst(
        candles,
        sma_period1=data.sma_period1,
        sma_period2=data.sma_period2,
        sma_period3=data.sma_period3,
        sma_period4=data.sma_period4,
        roc_period1=data.roc_period1,
        roc_period2=data.roc_period2,
        roc_period3=data.roc_period3,
        roc_period4=data.roc_period4,
        signal_period=data.signal_period,
        source_type=data.source_type
    )

    return {
        "indicator": "kst",
        "symbol": data.symbol,
        "interval": data.interval,
        "periods": {
            "sma": [data.sma_period1, data.sma_period2, data.sma_period3, data.sma_period4],
            "roc": [data.roc_period1, data.roc_period2, data.roc_period3, data.roc_period4],
            "signal": data.signal_period
        },
        "values": result
    }



# Mass Index 
@app.post("/mass")
async def get_mass(data: IndicatorRequest):
    candles = await fetch_candles(data.symbol, data.interval, data.limit)
    values = calculate_mass(candles, data.period, sequential=True)

    return {
        "indicator": "mass",
        "symbol": data.symbol.upper(),
        "interval": data.interval,
        "period": data.period,
        "values": values
    }



# McGinley Dynamic
@app.post("/mcginley")
async def get_mcginley(data: McGinleyRequest):
    candles = await fetch_candles(data.symbol, data.interval, data.limit)
    values = calculate_mcginley(
        candles=candles,
        period=data.period,
        k=data.k,
        source_type=data.source_type,
        sequential=data.sequential
    )

    return {
        "indicator": "mcginley_dynamic",
        "symbol": data.symbol.upper(),
        "interval": data.interval,
        "period": data.period,
        "k": data.k,
        "source_type": data.source_type,
        "values": values
    }



# Moving Average (MA)
@app.post("/ma")
async def get_ma(data: MARequest):
    candles = await fetch_candles(data.symbol, data.interval, data.limit)
    values = calculate_ma(
        candles=candles,
        period=data.period,
        matype=data.matype,
        source_type=data.source_type,
        sequential=data.sequential
    )

    return {
        "indicator": "ma",
        "symbol": data.symbol.upper(),
        "interval": data.interval,
        "period": data.period,
        "matype": data.matype,
        "source_type": data.source_type,
        "values": values
    }



# Mean Absolute Deviation
@app.post("/mean_ad")
async def get_mean_ad(data: IndicatorWithSourceRequest):
    candles = await fetch_candles(data.symbol, data.interval, data.limit)
    values = calculate_mean_ad(
        candles=candles,
        period=data.period,
        source_type=data.source_type,
        sequential=True  # fixed to always return array
    )

    return {
        "indicator": "mean_ad",
        "symbol": data.symbol.upper(),
        "interval": data.interval,
        "period": data.period,
        "source_type": data.source_type,
        "values": values
    }




# Median Absolute Deviation 
@app.post("/median_ad")
async def get_median_ad(data: IndicatorWithSourceRequest):
    candles = await fetch_candles(data.symbol, data.interval, data.limit)
    values = calculate_median_ad(
        candles=candles,
        period=data.period,
        source_type=data.source_type,
        sequential=True  # always return array
    )

    return {
        "indicator": "median_ad",
        "symbol": data.symbol.upper(),
        "interval": data.interval,
        "period": data.period,
        "source_type": data.source_type,
        "values": values
    }



# Median Price (MEDPRICE)
@app.post("/medprice")
async def get_medprice(data: NoPeriodIndicatorRequest):
    candles = await fetch_candles(data.symbol, data.interval, data.limit)
    values = calculate_medprice(
        candles=candles,
        sequential=True
    )

    return {
        "indicator": "medprice",
        "symbol": data.symbol.upper(),
        "interval": data.interval,
        "values": values
    }



# Momentum (MOM) 
@app.post("/mom")
async def get_mom(data: IndicatorWithSourceRequest):
    candles = await fetch_candles(data.symbol, data.interval, data.limit)
    values = calculate_mom(
        candles=candles,
        period=data.period,
        source_type=data.source_type,
        sequential=True  # always array
    )

    return {
        "indicator": "mom",
        "symbol": data.symbol.upper(),
        "interval": data.interval,
        "period": data.period,
        "source_type": data.source_type,
        "values": values
    }



# Weighted Moving Average (WMA)
@app.post("/wma")
async def get_wma(data: IndicatorWithSourceRequest):
    candles = await fetch_candles(data.symbol, data.interval, data.limit)
    values = calculate_wma(
        candles=candles,
        period=data.period,
        source_type=data.source_type,
        sequential=True
    )

    return {
        "indicator": "wma",
        "symbol": data.symbol.upper(),
        "interval": data.interval,
        "period": data.period,
        "source_type": data.source_type,
        "values": values
    }



# Parabolic SAR (SAR)
@app.post("/sar")
async def get_sar(data: SARRequest):
    candles = await fetch_candles(data.symbol, data.interval, data.limit)
    values = calculate_sar(
        candles=candles,
        acceleration=data.acceleration,
        maximum=data.maximum,
        sequential=data.sequential
    )

    return {
        "indicator": "sar",
        "symbol": data.symbol.upper(),
        "interval": data.interval,
        "acceleration": data.acceleration,
        "maximum": data.maximum,
        "values": values
    }



# Pivot Points
@app.post("/pivot")
async def get_pivot(data: PivotRequest):
    candles = await fetch_candles(data.symbol, data.interval, data.limit)
    values = calculate_pivot(
        candles=candles,
        mode=data.mode,
        sequential=data.sequential
    )

    return {
        "indicator": "pivot",
        "symbol": data.symbol.upper(),
        "interval": data.interval,
        "mode": data.mode,
        "values": values
    }



# Ultimate Oscillator (ULTOSC)
@app.post("/ultosc")
async def get_ultosc(data: ULTOSCRequest):
    candles = await fetch_candles(data.symbol, data.interval, data.limit)
    values = calculate_ultosc(
        candles=candles,
        timeperiod1=data.timeperiod1,
        timeperiod2=data.timeperiod2,
        timeperiod3=data.timeperiod3,
        sequential=data.sequential
    )

    return {
        "indicator": "ultosc",
        "symbol": data.symbol.upper(),
        "interval": data.interval,
        "timeperiod1": data.timeperiod1,
        "timeperiod2": data.timeperiod2,
        "timeperiod3": data.timeperiod3,
        "values": values
    }



# Volume Price Trend (VPT)
@app.post("/vpt")
async def get_vpt(data: VPTRequest):
    candles = await fetch_candles(data.symbol, data.interval, data.limit)
    values = calculate_vpt(
        candles=candles,
        source_type=data.source_type,
        sequential=data.sequential
    )

    return {
        "indicator": "vpt",
        "symbol": data.symbol.upper(),
        "interval": data.interval,
        "source_type": data.source_type,
        "values": values
    }



# Rate of Change Percentage (ROCP)
@app.post("/rocp")
async def get_rocp(data: IndicatorWithSourceRequest):
    candles = await fetch_candles(data.symbol, data.interval, data.limit)
    values = calculate_rocp(
        candles=candles,
        period=data.period,
        source_type=data.source_type,
        sequential=True
    )

    return {
        "indicator": "rocp",
        "symbol": data.symbol.upper(),
        "interval": data.interval,
        "period": data.period,
        "source_type": data.source_type,
        "values": values
    }



# Rate of Change Ratio (ROCR)
@app.post("/rocr")
async def get_rocr(data: IndicatorWithSourceRequest):
    candles = await fetch_candles(data.symbol, data.interval, data.limit)
    values = calculate_rocr(
        candles=candles,
        period=data.period,
        source_type=data.source_type,
        sequential=True
    )

    return {
        "indicator": "rocr",
        "symbol": data.symbol.upper(),
        "interval": data.interval,
        "period": data.period,
        "source_type": data.source_type,
        "values": values
    }



#  Rate of Change Ratio 100
@app.post("/rocr100")
async def get_rocr100(data: IndicatorWithSourceRequest):
    candles = await fetch_candles(data.symbol, data.interval, data.limit)
    values = calculate_rocr100(
        candles=candles,
        period=data.period,
        source_type=data.source_type,
        sequential=True
    )

    return {
        "indicator": "rocr100",
        "symbol": data.symbol.upper(),
        "interval": data.interval,
        "period": data.period,
        "source_type": data.source_type,
        "values": values
    }



# Relative Volatility Index (RVI)
@app.post("/rvi")
async def get_rvi(data: RVIRequest):
    candles = await fetch_candles(data.symbol, data.interval, data.limit)
    values = calculate_rvi(
        candles=candles,
        period=data.period,
        ma_len=data.ma_len,
        matype=data.matype,
        devtype=data.devtype,
        source_type=data.source_type,
        sequential=data.sequential
    )

    return {
        "indicator": "rvi",
        "symbol": data.symbol.upper(),
        "interval": data.interval,
        "period": data.period,
        "ma_len": data.ma_len,
        "matype": data.matype,
        "devtype": data.devtype,
        "source_type": data.source_type,
        "values": values
    }



# Smoothed Moving Average (SMMA)
@app.post("/smma")
async def get_smma(data: IndicatorWithSourceRequest):
    candles = await fetch_candles(data.symbol, data.interval, data.limit)
    values = calculate_smma(
        candles=candles,
        period=data.period,
        source_type=data.source_type,
        sequential=True
    )

    return {
        "indicator": "smma",
        "symbol": data.symbol.upper(),
        "interval": data.interval,
        "period": data.period,
        "source_type": data.source_type,
        "values": values
    }



# Stochastic Oscillator
@app.post("/stoch")
async def get_stoch(data: StochRequest):
    candles = await fetch_candles(data.symbol, data.interval, data.limit)
    values = calculate_stoch(
        candles=candles,
        fastk_period=data.fastk_period,
        slowk_period=data.slowk_period,
        slowk_matype=data.slowk_matype,
        slowd_period=data.slowd_period,
        slowd_matype=data.slowd_matype,
        sequential=data.sequential
    )

    return {
        "indicator": "stoch",
        "symbol": data.symbol.upper(),
        "interval": data.interval,
        "fastk_period": data.fastk_period,
        "slowk_period": data.slowk_period,
        "slowk_matype": data.slowk_matype,
        "slowd_period": data.slowd_period,
        "slowd_matype": data.slowd_matype,
        "values": values
    }



# True Strength Index (TSI)
@app.post("/tsi")
async def get_tsi(data: TSIRequest):
    candles = await fetch_candles(data.symbol, data.interval, data.limit)
    tsi_values = calculate_tsi(
        candles=candles,
        long_period=data.long_period,
        short_period=data.short_period,
        source_type=data.source_type,
        sequential=True
    )
    return {
        "indicator": "tsi",
        "symbol": data.symbol.upper(),
        "interval": data.interval,
        "long_period": data.long_period,
        "short_period": data.short_period,
        "source_type": data.source_type,
        "values": tsi_values
    }



# TTM Trend indicator
@app.post("/ttm_trend")
async def get_ttm_trend(data: IndicatorWithSourceRequest):
    candles = await fetch_candles(data.symbol, data.interval, data.limit)
    values = calculate_ttm_trend(
        candles=candles,
        period=data.period,
        source_type=data.source_type,
        sequential=True
    )
    return {
        "indicator": "ttm_trend",
        "symbol": data.symbol.upper(),
        "interval": data.interval,
        "period": data.period,
        "source_type": data.source_type,
        "values": values
    }



# Triple Exponential Moving Average (TEMA) 
@app.post("/tema")
async def get_tema(data: IndicatorWithSourceRequest):
    candles = await fetch_candles(data.symbol, data.interval, data.limit)

    values = calculate_tema(
        candles,
        period=data.period,
        source_type=data.source_type,
        sequential=True
    )

    return {
        "indicator": "tema",
        "symbol": data.symbol.upper(),
        "interval": data.interval,
        "period": data.period,
        "source_type": data.source_type,
        "values": values
    }



# TRIX - 1-day Rate-Of-Change (ROC) of a Triple Smooth EMA
@app.post("/trix")
async def get_trix(data: IndicatorWithSourceRequest):
    candles = await fetch_candles(data.symbol, data.interval, data.limit)
    values = calculate_trix(
        candles,
        period=data.period,
        source_type=data.source_type,
        sequential=True  # or False depending on use case
    )
    return {
        "indicator": "trix",
        "symbol": data.symbol.upper(),
        "interval": data.interval,
        "period": data.period,
        "source_type": data.source_type,
        "values": values
    }



# Volume
@app.post("/volume")
async def get_volume(data: IndicatorRequest):
    candles = await fetch_candles(data.symbol, data.interval, data.limit)
    values = calculate_volume(candles, data.period, sequential=True)

    return {
        "indicator": "volume",
        "symbol": data.symbol,
        "interval": data.interval,
        "period": data.period,
        "values": values
    }



# ariable Power Weighted Moving Average (VPWMA)
@app.post("/vpwma")
async def get_vpwma(data: VPWMARequest):
    candles = await fetch_candles(data.symbol, data.interval, data.limit)
    values = calculate_vpwma(
        candles,
        period=data.period,
        power=data.power,
        source_type=data.source_type,
        sequential=False
    )
    return {
        "indicator": "vpwma",
        "symbol": data.symbol,
        "interval": data.interval,
        "period": data.period,
        "power": data.power,
        "source_type": data.source_type,
        "values": values
    }



# Volume Weighted Moving Average (VWMA)
@app.post("/vwma")
async def get_vwma(data: IndicatorWithSourceRequest):
    candles = await fetch_candles(data.symbol, data.interval, data.limit)
    vwma_values = calculate_vwma(
        candles,
        period=data.period,
        source_type=data.source_type,
        sequential=True
    )

    return {
        "indicator": "vwma",
        "symbol": data.symbol.upper(),
        "interval": data.interval,
        "period": data.period,
        "source_type": data.source_type,
        "values": vwma_values
    }














