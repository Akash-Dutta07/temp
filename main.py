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
from models.indicator_request import SourceOnlyRequest
from models.indicator_request import ALMARequest
from models.indicator_request import BetaRequest
from models.indicator_request import KDJRequest
from models.indicator_request import KVORequest
from models.indicator_request import MWDXRequest
from models.indicator_request import NVIRequest
from models.indicator_request import PVIRequest
from models.indicator_request import DecOscRequest
from models.indicator_request import SafeZoneStopRequest
from models.indicator_request import SupportResistanceBreaksRequest
from models.indicator_request import TTMSqueezeRequest
from models.indicator_request import WTRequest
from models.indicator_request import Volume24hRequest

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
from indicators.chop import calculate_chop
from indicators.correl import calculate_correl
from indicators.dpo import calculate_dpo
from indicators.dm import calculate_dm
from indicators.aroon import calculate_aroon
from indicators.ao import calculate_ao
from indicators.bop import calculate_bop
from indicators.ad import calculate_ad
from indicators.bollinger_bands_width import calculate_bollinger_bands_width
from indicators.cfo import calculate_cfo
from indicators.adosc import calculate_adosc
from indicators.dx import calculate_dx
from indicators.dema import calculate_dema
from indicators.fisher import calculate_fisher
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
from indicators.alligator import calculate_alligator
from indicators.alma import calculate_alma
from indicators.beta import calculate_beta
from indicators.avgprice import calculate_avgprice
from indicators.hma import calculate_hma
from indicators.kdj import calculate_kdj
from indicators.kvo import calculate_kvo
from indicators.linearreg import calculate_linearreg
from indicators.mwdx import calculate_mwdx
from indicators.nvi import calculate_nvi
from indicators.pvi import calculate_pvi
from indicators.dec_osc import calculate_dec_osc
from indicators.safezonestop import calculate_safezonestop
from indicators.support_resistance_with_breaks import calculate_support_resistance_with_breaks
from indicators.tsf import calculate_tsf
from indicators.ttm_squeeze import calculate_ttm_squeeze
from indicators.vi import calculate_vi
from indicators.wt import calculate_wt
from indicators.srsi import calculate_srsi
from indicators.volume_24h import calculate_volume_24h

import numpy as np
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

# NEW WEBSOCKET IMPORTS
import asyncio
import json
import inspect
from fastapi import WebSocket, WebSocketDisconnect
from fastapi.encoders import jsonable_encoder
from utils.websocket_manager import manager


# Indicator Functions Mapping 
INDICATOR_FUNCTIONS = {
    "ad": calculate_ad,
    "adosc": calculate_adosc,
    "adx": calculate_adx,
    "alligator": calculate_alligator,
    "alma": calculate_alma,
    "ao": calculate_ao,
    "apo": calculate_apo,
    "aroon": calculate_aroon,
    "atr": calculate_atr,
    "avgprice": calculate_avgprice,
    "beta": calculate_beta,
    "bollinger_bands_width": calculate_bollinger_bands_width,
    "bollinger_bands": calculate_bollinger_bands,
    "bop": calculate_bop,
    "fisher": calculate_fisher,
    "cc": calculate_cc,
    "cci": calculate_cci,
    "cfo": calculate_cfo,
    "chop": calculate_chop,
    "cksp": calculate_cksp,
    "cmo": calculate_cmo,
    "correl": calculate_correl,
    "decosc": calculate_dec_osc,
    "dema": calculate_dema,
    "di": calculate_di,
    "dm": calculate_dm,
    "donchian": calculate_donchian,
    "dpo": calculate_dpo,
    "dx": calculate_dx,
    "efi": calculate_efi,
    "ema": calculate_ema,
    "emv": calculate_emv,
    "hma": calculate_hma,
    "ichimoku_cloud": calculate_ichimoku_cloud,
    "kdj": calculate_kdj,
    "keltner": calculate_keltner,
    "kst": calculate_kst,
    "kvo": calculate_kvo,
    "linearreg": calculate_linearreg,
    "ma": calculate_ma,
    "macd": calculate_macd,
    "mass": calculate_mass,
    "mcginley_dynamic": calculate_mcginley,
    "mean_ad": calculate_mean_ad,
    "median_ad": calculate_median_ad,
    "medprice": calculate_medprice,
    "mfi": calculate_mfi,
    "mom": calculate_mom,
    "mwdx": calculate_mwdx,
    "nvi": calculate_nvi,
    "obv": calculate_obv,
    "pivot": calculate_pivot,
    "ppo": calculate_ppo,
    "pvi": calculate_pvi,
    "roc": calculate_roc,
    "rocp": calculate_rocp,
    "rocr": calculate_rocr,
    "rocr100": calculate_rocr100,
    "rsi": calculate_rsi,
    "rvi": calculate_rvi,
    "safezonestop": calculate_safezonestop,
    "sar": calculate_sar,
    "sma": calculate_sma,
    "smma": calculate_smma,
    "stoch": calculate_stoch,
    "srsi": calculate_srsi,
    "supertrend": calculate_supertrend,
    "support_resistance_with_breaks": calculate_support_resistance_with_breaks,
    "tema": calculate_tema,
    "trix": calculate_trix,
    "tsf": calculate_tsf,
    "tsi": calculate_tsi,
    "ttm_squeeze": calculate_ttm_squeeze,
    "ttm_trend": calculate_ttm_trend,
    "ultosc": calculate_ultosc,
    "vi": calculate_vi,
    "volume_24h": calculate_volume_24h,
    "volume": calculate_volume,
    "vpt": calculate_vpt,
    "vpwma": calculate_vpwma,
    "vwap": calculate_vwap,
    "vwma": calculate_vwma,
    "williams_r": calculate_williams_r,
    "wma": calculate_wma,
    "wt": calculate_wt,
}


app = FastAPI()
# Allow CORS for  frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173","http://localhost:5174"],  # or ["*"] to allow all (not recommended for production)
    allow_credentials=True,
    allow_methods=["*"],                      # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],                      # Allow all headers
)


# WebSocket Endpoint 
@app.websocket("/ws/indicators")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        config_message = await websocket.receive_text()
        config = json.loads(config_message)

        indicator_name = config.get("indicator").lower()
        symbol = config.get("symbol")
        interval = config.get("interval")
        limit = config.get("limit", 200)

        if not all([indicator_name, symbol, interval]):
            await manager.send_personal_message({"error": "Missing required parameters."}, websocket)
            return

        if indicator_name not in INDICATOR_FUNCTIONS:
            await manager.send_personal_message({"error": f"Unknown indicator: {indicator_name}"}, websocket)
            return

        calculate_function = INDICATOR_FUNCTIONS[indicator_name]
        
        while True:
            try:
                candles = await fetch_candles(symbol=symbol, interval=interval, limit=limit)
                
                func_params = inspect.signature(calculate_function).parameters
                
                calc_args = {"candles": candles}
                
                for key, value in config.items():
                    if key in func_params:
                        calc_args[key] = value

                if 'sequential' in func_params:
                    calc_args['sequential'] = True
                
                result_values = calculate_function(**calc_args)

                data_to_send = {
                    "indicator": indicator_name,
                    "symbol": symbol.upper(),
                    "interval": interval,
                    "values": jsonable_encoder(result_values)
                }

                # This try...except block is the core fix. It will break the loop immediately
                # if the client disconnects, preventing the RuntimeError.
                try:
                    await manager.send_personal_message(data_to_send, websocket)
                except WebSocketDisconnect:
                    print(f"Client disconnected from {websocket.client}")
                    break # Exit the loop immediately on disconnection

            except Exception as e:
                print(f"Error for {symbol} ({indicator_name}): {e}")
                await manager.send_personal_message({"error": f"Failed to calculate {indicator_name}: {str(e)}"}, websocket)

            await asyncio.sleep(5)

    except WebSocketDisconnect:
        print(f"Client disconnected from {websocket.client}")
    except json.JSONDecodeError:
        print("Received invalid JSON from client.")
        await manager.send_personal_message({"error": "Invalid JSON format received."}, websocket)
    finally:
        manager.disconnect(websocket)
        print("Connection closed.")







# Simple Moving Average (SMA)
@app.post("/sma")
async def get_sma(data: IndicatorWithSourceRequest):
    """Simple Moving Average (SMA)"""
    candles = await fetch_candles(data.symbol, data.interval, data.limit)
    values = calculate_sma(
        candles=candles,
        period=data.period,
        source_type=data.source_type,
        sequential=data.sequential  # always array output
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
    """Relative Strength Index (RSI) """
    candles = await fetch_candles(data.symbol, data.interval, data.limit)
    values = calculate_rsi(
        candles=candles,
        period=data.period,
        source_type=data.source_type,
        sequential=data.sequential  # array output
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
    """Exponential Moving Average (EMA)"""
    candles = await fetch_candles(data.symbol, data.interval, data.limit)
    values = calculate_ema(candles, period=data.period, source_type=data.source_type, sequential=data.sequential)
    
    return {
        "indicator": "ema",
        "symbol": data.symbol.upper(),
        "interval": data.interval,
        "period": data.period,
        "source_type": data.source_type,
        "values": values
    }

# Moving Average Convergence Divergence (MACD)
@app.post("/macd")
async def get_macd(data: MACDRequest):
    """Moving Average Convergence Divergence (MACD)"""
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
    """Bollinger Bands"""
    candles = await fetch_candles(data.symbol, data.interval, data.limit)

    values = calculate_bollinger_bands(
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
        "values": values
    }

#Average True Range (ATR)
@app.post("/atr")
async def get_atr(data: IndicatorRequest):
    """Average True Range (ATR))"""
    candles = await fetch_candles(data.symbol, data.interval, data.limit)
    values = calculate_atr(
        candles=candles,
        period=data.period,
        sequential=data.sequential  # always array output
    )

    return {
        "indicator": "atr",
        "symbol": data.symbol.upper(),
        "interval": data.interval,
        "period": data.period,
        "values": values
    }

# SuperTrend
@app.post("/supertrend")
async def get_supertrend(data: SupertrendRequest):
    """SuperTrend"""
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
    """Volume Weighted Average Price (VWAP"""
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
    """Average Directional Movement Index (ADX)"""
    candles = await fetch_candles(data.symbol, data.interval, data.limit)
    values = calculate_adx(
        candles=candles,
        period=data.period,
        sequential=data.sequential  # always array output
    )

    return {
        "indicator": "adx",
        "symbol": data.symbol.upper(),
        "interval": data.interval,
        "period": data.period,
        "values": values
    }

# Commodity Channel Index (CCI)
@app.post("/cci")
async def get_cci(data: IndicatorRequest):
    """Commodity Channel Index"""
    candles = await fetch_candles(data.symbol, data.interval, data.limit)
    values = calculate_cci(
        candles=candles,
        period=data.period,
        sequential=data.sequential  # always array output
    )

    return {
        "indicator": "cci",
        "symbol": data.symbol.upper(),
        "interval": data.interval,
        "period": data.period,
        "values": values
    }

# Williams' %R(willr)
@app.post("/williams_r")
async def get_williams_r(data: IndicatorRequest):
    """Williams' %R (willr)"""
    candles = await fetch_candles(data.symbol, data.interval, data.limit)
    values = calculate_williams_r(
        candles=candles,
        period=data.period,
        sequential=data.sequential  # always array output
    )

    return {
        "indicator": "williams_r",
        "symbol": data.symbol.upper(),
        "interval": data.interval,
        "period": data.period,
        "values": values
    }   

#  Rate of Change (ROC)
@app.post("/roc")
async def get_roc(data: IndicatorWithSourceRequest):
    candles = await fetch_candles(data.symbol, data.interval, data.limit)
    values = calculate_roc(
        candles=candles,
        period=data.period,
        source_type=data.source_type,
        sequential=data.sequential  # return array
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
    """Chande Momentum Oscillator (CMO)"""
    candles = await fetch_candles(data.symbol, data.interval, data.limit)
    values = calculate_cmo(
        candles=candles,
        period=data.period,
        source_type=data.source_type,
        sequential=data.sequential
    )

    return {
        "indicator": "cmo",
        "symbol": data.symbol.upper(),
        "interval": data.interval,
        "period": data.period,
        "source_type": data.source_type,
        "values": values
    }

# Absolute Price Oscillator (APO)
@app.post("/apo")
async def get_apo(data: APORequest):
    """Absolute Price Oscillator (APO)"""
    candles = await fetch_candles(data.symbol, data.interval, data.limit)

    values = calculate_apo(
        candles=candles,
        fast_period=data.fast_period,
        slow_period=data.slow_period,
        matype=data.matype,
        source_type=data.source_type,
        sequential=data.sequential
    )

    return {
        "indicator": "apo",
        "symbol": data.symbol.upper(),
        "interval": data.interval,
        "fast_period": data.fast_period,
        "slow_period": data.slow_period,
        "matype": data.matype,
        "source_type": data.source_type,
        "values": values
    }

# Percentage Price Oscillator (PPO)
@app.post("/ppo")
async def get_ppo(data: PPORequest):
    """Percentage Price Oscillator (PPO)"""
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
    """Money Flow Index (MFI)"""
    candles = await fetch_candles(data.symbol, data.interval, data.limit)
    values = calculate_mfi(candles=candles, period=data.period, sequential=data.sequential)

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
    """Coppock Curve(CC)"""
    candles = await fetch_candles(data.symbol, data.interval, data.limit)
    values = calculate_cc(
        candles=candles,
        wma_period=data.wma_period,
        roc_short_period=data.roc_short_period,
        roc_long_period=data.roc_long_period,
        source_type=data.source_type,
        sequential=data.sequential
    )

    return {
        "indicator": "cc",
        "symbol": data.symbol.upper(),
        "interval": data.interval,
        "wma_period": data.wma_period,
        "roc_short_period": data.roc_short_period,
        "roc_long_period": data.roc_long_period,
        "values": values
    }

# Donchian Channels (donchian)
@app.post("/donchian")
async def get_donchian(data: IndicatorRequest):
    """Donchian Channels"""
    candles = await fetch_candles(data.symbol, data.interval, data.limit)
    values = calculate_donchian(
        candles=candles,
        period=data.period,
        sequential=data.sequential
    )

    return {
        "indicator": "dochian",
        "symbol": data.symbol.upper(),
        "interval": data.interval,
        "period": data.period,
        "values": values
    }

# On Balance Volume (OBV)
@app.post("/obv")
async def get_obv(data: NoPeriodIndicatorRequest):
    """On Balance Volume (OBV)"""
    candles = await fetch_candles(data.symbol, data.interval, data.limit)
    values = calculate_obv(candles=candles, sequential=data.sequential)

    return {
        "indicator": "obv",
        "symbol": data.symbol.upper(),
        "interval": data.interval,
        "values": values
    }

# Elder's Force Index (EFI)
@app.post("/efi")
async def get_efi(data: IndicatorWithSourceRequest):
    """Elder's Force Index (EFI)"""
    candles = await fetch_candles(data.symbol, data.interval, data.limit)
    values = calculate_efi(
        candles=candles,
        period=data.period,
        source_type=data.source_type,
        sequential=data.sequential
    )

    return {
        "indicator": "efi",
        "symbol": data.symbol.upper(),
        "interval": data.interval,
        "period": data.period,
        "source_type": data.source_type,
        "values": values
    }

# Aroon indicator
@app.post("/aroon")
async def get_aroon(data: IndicatorRequest):
    """ aroon - Aroon indicator"""
    candles = await fetch_candles(data.symbol, data.interval, data.limit)
    values = calculate_aroon(
        candles=candles,
        period=data.period,
        sequential=data.sequential
    )

    return {
        "indicator": "aroon",
        "symbol": data.symbol.upper(),
        "interval": data.interval,
        "period": data.period,
        "values": values
    }

# Awesome Oscillator (ao)
@app.post("/ao")
async def get_ao(data: NoPeriodIndicatorRequest):
    """Ao -Awesome Oscillator"""
    candles = await fetch_candles(data.symbol, data.interval, data.limit)
    values = calculate_ao(
        candles=candles,
        sequential=data.sequential
    )

    return {
        "indicator": "ao",
        "symbol": data.symbol.upper(),
        "interval": data.interval,
        "values": values
    }

# Balance of Power (BOP)
@app.post("/bop")
async def get_bop(data: NoPeriodIndicatorRequest):
    """BOP - Balance of Power"""
    candles = await fetch_candles(data.symbol, data.interval, data.limit)
    values = calculate_bop(candles=candles, sequential=data.sequential)

    return {
        "indicator": "bop",
        "symbol": data.symbol.upper(),
        "interval": data.interval,
        "values": values
    }

# Accumulation/Distribution Line (AD)
@app.post("/ad")
async def get_ad(data: NoPeriodIndicatorRequest):
    """AD - Accumulation/Distribution Line"""
    candles = await fetch_candles(data.symbol, data.interval, data.limit)
    values = calculate_ad(candles=candles, sequential=data.sequential)
    return {
        "indicator": "ad",
        "symbol": data.symbol.upper(),
        "interval": data.interval,
        "values": values
    }


# Bollinger Bands Width
@app.post("/bollinger-bands-width")
async def get_bollinger_bands_width(data: BollingerBandsWidthRequest):
    """Bollinger Bands Bandwidth"""
    candles = await fetch_candles(data.symbol, data.interval, data.limit)
    values = calculate_bollinger_bands_width(
        candles=candles,
        period=data.period,
        mult=data.mult,
        source_type=data.source_type,
        sequential=data.sequential
    )

    return {
        "indicator": "bollinger_bands_width",
        "symbol": data.symbol.upper(),
        "interval": data.interval,
        "period": data.period,
        "mult": data.mult,
        "source_type": data.source_type,
        "values": values
    }

# Chande Forecast Oscillator (CFO)   
@app.post("/cfo")
async def get_cfo(data: CFORequest):
    """Chande Forecast Oscillator (CFO)"""
    candles = await fetch_candles(data.symbol, data.interval, data.limit)
    result = calculate_cfo(candles=candles, period=data.period, scalar=data.scalar, source_type=data.source_type, sequential=data.sequential)

    return {
        "indicator": "cfo",
        "symbol": data.symbol.upper(),
        "interval": data.interval,
        "period": data.period,
        "scalar": data.scalar,
        "values": result
    }

# Chaikin A/D Oscillator(adosc)
@app.post("/adosc")
async def get_adosc(data: ADOSCRequest):
    """ADOSC - Chaikin Oscillator"""
    candles = await fetch_candles(data.symbol, data.interval, data.limit)
    values = calculate_adosc(candles=candles, fast_period=data.fast_period, slow_period=data.slow_period, sequential=data.sequential)
    return {
        "indicator": "adosc",
        "symbol": data.symbol.upper(),
        "interval": data.interval,
        "fast_period": data.fast_period,
        "slow_period": data.slow_period,
        "values": values 
    }


# Chande Kroll Stop (CKSP)
@app.post("/cksp")
async def get_cksp(data: CKSPRequest):
    """Chande Kroll Stop (CKSP)"""
    candles = await fetch_candles(data.symbol, data.interval, data.limit)
    values = calculate_cksp(
        candles=candles,
        p=data.p,
        x=data.x,
        q=data.q,
        sequential=data.sequential
    )

    return {
        "indicator": "cksp",
        "symbol": data.symbol.upper(),
        "interval": data.interval,
        "values": values
    }


# Choppiness Index (CHOP)  
@app.post("/chop")
async def get_chop(data: CHOPRequest):
    """Choppiness Index (CHOP)"""
    candles = await fetch_candles(data.symbol, data.interval, data.limit)
    values = calculate_chop(candles=candles, period=data.period, scalar=data.scalar, drift=data.drift, sequential=data.sequential)

    return {
        "indicator": "chop",
        "symbol": data.symbol.upper(),
        "interval": data.interval,
        "period": data.period,
        "scalar": data.scalar,
        "drift": data.drift,
        "values": values
    }


# Pearson's Correlation Coefficient
@app.post("/correl")
async def get_correl(data: IndicatorRequest):
    """Pearson's Correlation Coefficient"""
    candles = await fetch_candles(data.symbol, data.interval, data.limit)
    values = calculate_correl(candles=candles, period=data.period, sequential=data.sequential)

    return {
        "indicator": "correl",
        "symbol": data.symbol.upper(),
        "interval": data.interval,
        "period": data.period,
        "values": values
    }


# Detrended Price Oscillator (DPO)
@app.post("/dpo")
async def get_dpo(data: IndicatorWithSourceRequest):
    """Detrended Price Oscillator (DPO)"""
    candles = await fetch_candles(data.symbol, data.interval, data.limit)
    values = calculate_dpo(
        candles=candles,
        period=data.period,
        source_type=data.source_type,
        sequential=data.sequential 
    )

    return {
        "indicator": "dpo",
        "symbol": data.symbol.upper(),
        "interval": data.interval,
        "period": data.period,
        "source_type": data.source_type,
        "values": values
    }



# Directional Movement (dm)
@app.post("/dm")
async def get_dm(data: IndicatorRequest):
    """Directional Movement"""
    candles = await fetch_candles(data.symbol, data.interval, data.limit)
    values = calculate_dm(candles=candles, period=data.period, sequential=data.sequential)

    return {
        "indicator": "dm",
        "symbol": data.symbol.upper(),
        "interval": data.interval,
        "period": data.period,
        "values": values
    }


#  Directional Movement Index (DMI) 
@app.post("/dx")
async def get_dx(data: DXRequest):
    """ Directional Movement Index (DMI)"""
    candles = await fetch_candles(data.symbol, data.interval, data.limit)
    values = calculate_dx(candles=candles, di_length=data.di_length, adx_smoothing=data.adx_smoothing, sequential=data.sequential)

    return {
        "indicator": "dx",
        "symbol": data.symbol.upper(),
        "interval": data.interval,
        "di_length": data.di_length,
        "adx_smoothing": data.adx_smoothing,
        "values": values
    }



# Double Exponential Moving Average (DEMA)
@app.post("/dema")
async def get_dema(data: IndicatorWithSourceRequest):
    candles = await fetch_candles(data.symbol, data.interval, data.limit)
    values = calculate_dema(
        candles=candles,
        period=data.period,
        source_type=data.source_type,
        sequential=data.sequential  
    )

    return {
        "indicator": "dema",
        "symbol": data.symbol.upper(),
        "interval": data.interval,
        "period": data.period,
        "source_type": data.source_type,
        "values": values
    }



#  Fisher Transform (fisher)
@app.post("/fisher")
async def get_fisher(data: IndicatorRequest):
    """Fisher Transform"""
    candles = await fetch_candles(data.symbol, data.interval, data.limit)
    values = calculate_fisher(candles=candles, period=data.period, sequential=data.sequential)

    return {
        "indicator": "fisher",
        "symbol": data.symbol.upper(),
        "interval": data.interval,
        "period": data.period,
        "values": values
    }


# ichimoku_cloud
@app.post("/ichimoku-cloud")
async def get_ichimoku_cloud(data: IchimokuCloudRequest):
    """ichimoku_cloud"""
    candles = await fetch_candles(data.symbol, data.interval, data.limit)
    values = calculate_ichimoku_cloud(
        candles,
        conversion_line_period=data.conversion_line_period,
        base_line_period=data.base_line_period,
        lagging_line_period=data.lagging_line_period,
        displacement=data.displacement,
        sequential=data.sequential
    )
    return {
        "indicator": "ichimoku_cloud",
        "symbol": data.symbol.upper(),
        "interval": data.interval,
        "values": values
    }



# Directional Indicator (di) 
@app.post("/di")
async def get_di(data: IndicatorRequest):
    """Directional Indicator"""
    candles = await fetch_candles(data.symbol, data.interval, data.limit)
    values = calculate_di(candles=candles, period=data.period, sequential=data.sequential)

    return {
        "indicator": "di",
        "symbol": data.symbol.upper(),
        "interval": data.interval,
        "period": data.period,
        "values": values
    }



#Ease of Movement (emv)
@app.post("/emv")
async def get_emv(data: IndicatorWithLengthAndDivRequest):
    """Ease of Movement"""
    candles = await fetch_candles(data.symbol, data.interval, data.limit)
    values = calculate_emv(candles=candles, length=data.length, div=data.div, sequential=data.sequential)
    
    return {
        "indicator": "emv",
        "symbol": data.symbol.upper(),
        "interval": data.interval,
        "length": data.length,
        "div": data.div,
        "values": values
    }



# Keltner Channels
@app.post("/keltner")
async def get_keltner(data: KeltnerRequest):
    """Keltner Channels"""
    candles = await fetch_candles(data.symbol, data.interval, data.limit)

    values = calculate_keltner(
        candles,
        period=data.period,
        multiplier=data.multiplier,
        matype=data.matype,
        source_type=data.source_type,
        sequential=data.sequential
    )
 
    return {
        "indicator": "keltner",
        "symbol": data.symbol.upper(),
        "interval": data.interval,
        "period": data.period,
        "multiplier": data.multiplier,
        "matype": data.matype,
        "values": values
    }



# KST (Know Sure Thing)
@app.post("/kst")
async def get_kst(data: KSTRequest):
    """Know Sure Thing (KST)"""
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
        source_type=data.source_type,
        sequential=data.sequential
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
    """Mass Index"""
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
    """McGinley Dynamic"""
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
    """Moving Averages"""
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
    """Mean Absolute Deviation"""
    candles = await fetch_candles(data.symbol, data.interval, data.limit)
    values = calculate_mean_ad(
        candles=candles,
        period=data.period,
        source_type=data.source_type,
        sequential=data.sequential  
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
    """Median Absolute Deviation"""
    candles = await fetch_candles(data.symbol, data.interval, data.limit)
    values = calculate_median_ad(
        candles=candles,
        period=data.period,
        source_type=data.source_type,
        sequential=data.sequential
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
    """Median Price (MEDPRICE)"""
    candles = await fetch_candles(data.symbol, data.interval, data.limit)
    values = calculate_medprice(
        candles=candles,
        sequential=data.sequential
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
    """Momentum (MOM)"""
    candles = await fetch_candles(data.symbol, data.interval, data.limit)
    values = calculate_mom(
        candles=candles,
        period=data.period,
        source_type=data.source_type,
        sequential=data.sequential
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
    """Weighted Moving Average (WMA)"""
    candles = await fetch_candles(data.symbol, data.interval, data.limit)
    values = calculate_wma(
        candles=candles,
        period=data.period,
        source_type=data.source_type,
        sequential=data.sequential
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
    """Parabolic SAR (SAR)"""
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
    """Pivot Points"""
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
    """Ultimate Oscillator (ULTOSC)"""
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
    """Volume Price Trend (VPT)"""
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
    """ Rate of Change Percentage (ROCP)"""
    candles = await fetch_candles(data.symbol, data.interval, data.limit)
    values = calculate_rocp(
        candles=candles,
        period=data.period,
        source_type=data.source_type,
        sequential=data.sequential
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
    """Rate of Change Ratio (ROCR)"""
    candles = await fetch_candles(data.symbol, data.interval, data.limit)
    values = calculate_rocr(
        candles=candles,
        period=data.period,
        source_type=data.source_type,
        sequential=data.sequential
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
    """Rate of Change Ratio 100"""
    candles = await fetch_candles(data.symbol, data.interval, data.limit)
    values = calculate_rocr100(
        candles=candles,
        period=data.period,
        source_type=data.source_type,
        sequential=data.sequential
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
    """Relative Volatility Index (RVI)"""
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
    """Smoothed Moving Average (SMMA)"""
    candles = await fetch_candles(data.symbol, data.interval, data.limit)
    values = calculate_smma(
        candles=candles,
        period=data.period,
        source_type=data.source_type,
        sequential=data.sequential
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
    """Stochastic Oscillator"""
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
    """True Strength Index (TSI)"""
    candles = await fetch_candles(data.symbol, data.interval, data.limit)
    tsi_values = calculate_tsi(
        candles=candles,
        long_period=data.long_period,
        short_period=data.short_period,
        source_type=data.source_type,
        sequential=data.sequential
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
    """TTM Trend indicator"""
    candles = await fetch_candles(data.symbol, data.interval, data.limit)
    values = calculate_ttm_trend(
        candles=candles,
        period=data.period,
        source_type=data.source_type,
        sequential=data.sequential
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
    """Triple Exponential Moving Average (TEMA)"""
    candles = await fetch_candles(data.symbol, data.interval, data.limit)

    values = calculate_tema(
        candles,
        period=data.period,
        source_type=data.source_type,
        sequential=data.sequential
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
    """TRIX - 1-day Rate-Of-Change (ROC)"""
    candles = await fetch_candles(data.symbol, data.interval, data.limit)
    values = calculate_trix(
        candles=candles,
        period=data.period,
        source_type=data.source_type,
        sequential=data.sequential
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
    """Volume"""
    candles = await fetch_candles(data.symbol, data.interval, data.limit)
    values = calculate_volume(candles=candles, period=data.period, sequential=data.sequential)

    return {
        "indicator": "volume",
        "symbol": data.symbol.upper(),
        "interval": data.interval,
        "period": data.period,
        "values": values
    }



# Variable Power Weighted Moving Average (VPWMA)
@app.post("/vpwma")
async def get_vpwma(data: VPWMARequest):
    """Variable Power Weighted Moving Average (VPWMA)"""
    candles = await fetch_candles(data.symbol, data.interval, data.limit)
    values = calculate_vpwma(
        candles=candles,
        period=data.period,
        power=data.power,
        source_type=data.source_type,
        sequential=data.sequential
    )
    return {
        "indicator": "vpwma",
        "symbol": data.symbol.upper(),
        "interval": data.interval,
        "period": data.period,
        "power": data.power,
        "source_type": data.source_type,
        "values": values
    }



# Volume Weighted Moving Average (VWMA)
@app.post("/vwma")
async def get_vwma(data: IndicatorWithSourceRequest):
    """Volume Weighted Moving Average (VWMA)"""
    candles = await fetch_candles(data.symbol, data.interval, data.limit)
    values = calculate_vwma(
        candles,
        period=data.period,
        source_type=data.source_type,
        sequential=data.sequential
    )

    return {
        "indicator": "vwma",
        "symbol": data.symbol.upper(),
        "interval": data.interval,
        "period": data.period,
        "source_type": data.source_type,
        "values": values
    }



# Alligator
@app.post("/alligator")
async def get_alligator(data: SourceOnlyRequest):
    """Alligator"""
    candles = await fetch_candles(data.symbol, data.interval, data.limit)
    values = calculate_alligator(
        candles,
        source_type=data.source_type,
        sequential=data.sequential
    )

    return {
        "indicator": "alligator",
        "symbol": data.symbol.upper(),
        "interval": data.interval,
        "source_type": data.source_type,
        "values": values
    }


# Arnaud Legoux Moving Average (ALMA)
@app.post("/alma")
async def get_alma(data: ALMARequest):
    """Arnaud Legoux Moving Average (ALMA)"""
    candles = await fetch_candles(data.symbol, data.interval, data.limit)
    values = calculate_alma(
        candles,
        period=data.period,
        sigma=data.sigma,
        distribution_offset=data.distribution_offset,
        source_type=data.source_type,
        sequential=data.sequential
    )

    return {
        "indicator": "alma",
        "symbol": data.symbol.upper(),
        "interval": data.interval,
        "params": {
            "period": data.period,
            "sigma": data.sigma,
            "distribution_offset": data.distribution_offset,
            "source_type": data.source_type
        },
        "values": values
    }



# beta
@app.post("/beta")
async def get_beta(data: BetaRequest):
    """Beta"""
    main_candles = await fetch_candles(data.symbol, data.interval, data.limit)
    benchmark_candles = await fetch_candles(data.benchmark_symbol, data.interval, data.limit)

    values = calculate_beta(
        main_candles,
        benchmark_candles,
        period=data.period,
        sequential=data.sequential
    )

    return {
        "indicator": "beta",
        "symbol": data.symbol.upper(),
        "benchmark_symbol": data.benchmark_symbol,
        "interval": data.interval,
        "period": data.period,
        "values": values
    }



# Average Price
@app.post("/avgprice")
async def get_avgprice(data: NoPeriodIndicatorRequest):
    """Average Price"""
    candles = await fetch_candles(data.symbol, data.interval, data.limit)

    values = calculate_avgprice(candles=candles, sequential=data.sequential)

    return {
        "indicator": "avgprice",
        "symbol": data.symbol.upper(),
        "interval": data.interval,
        "values": values
    }



# Hull Moving Average (HMA)
@app.post("/hma")
async def get_hma(data: IndicatorWithSourceRequest):
    """Hull Moving Average (HMA)"""
    candles = await fetch_candles(data.symbol, data.interval, data.limit)

    values = calculate_hma(
        candles=candles,
        period=data.period,
        source_type=data.source_type,
        sequential=data.sequential
    )

    return {
        "indicator": "hma",
        "symbol": data.symbol.upper(),
        "interval": data.interval,
        "period": data.period,
        "source_type": data.source_type,
        "values": values
    }
    


#  KDJ Oscillator
@app.post("/kdj")
async def get_kdj(data: KDJRequest):
    """KDJ Oscillator"""
    candles = await fetch_candles(data.symbol, data.interval, data.limit)

    values = calculate_kdj(
        candles=candles,
        fastk_period=data.fastk_period,
        slowk_period=data.slowk_period,
        slowk_matype=data.slowk_matype,
        slowd_period=data.slowd_period,
        slowd_matype=data.slowd_matype,
        sequential=data.sequential
    )

    return {
        "indicator": "kdj",
        "symbol": data.symbol.upper(),
        "interval": data.interval,
        "values": values
    }


# Klinger Volume Oscillator (KVO)
@app.post("/kvo")
async def get_kvo(data: KVORequest):
    """Klinger Volume Oscillator (KVO)"""
    candles = await fetch_candles(data.symbol, data.interval, data.limit)

    values = calculate_kvo(
        candles=candles,
        short_period=data.short_period,
        long_period=data.long_period,
        sequential=data.sequential
    )

    return {
        "indicator": "kvo",
        "symbol": data.symbol.upper(),
        "interval": data.interval,
        "short_period": data.short_period,
        "long_period": data.long_period,
        "values": values
    }


# Linear Regression indicator (LINEARREG)
@app.post("/linearreg")
async def get_linearreg(data: IndicatorWithSourceRequest):
    """Linear Regression indicator (LINEARREG)"""
    candles = await fetch_candles(data.symbol, data.interval, data.limit)

    values = calculate_linearreg(
        candles=candles,
        period=data.period,
        source_type=data.source_type,
        sequential=data.sequential
    )

    return {
        "indicator": "linearreg",
        "symbol": data.symbol.upper(),
        "interval": data.interval,
        "period": data.period,
        "source_type": data.source_type,
        "values": values
    }


# MWDX Average
@app.post("/mwdx")
async def get_mwdx(data: MWDXRequest):
    """MWDX Average"""
    candles = await fetch_candles(data.symbol, data.interval, data.limit)

    values = calculate_mwdx(
        candles=candles,
        factor=data.factor,
        source_type=data.source_type,
        sequential=data.sequential
    )

    return {
        "indicator": "mwdx",
        "symbol": data.symbol.upper(),
        "interval": data.interval,
        "factor": data.factor,
        "source_type": data.source_type,
        "values": values
    }

# Negative Volume Index (NVI)
@app.post("/nvi")
async def get_nvi(data: NVIRequest):
    """Negative Volume Index (NVI)"""
    candles = await fetch_candles(data.symbol, data.interval, data.limit)

    values = calculate_nvi(
        candles=candles,
        source_type=data.source_type,
        sequential=data.sequential
    )

    return {
        "indicator": "nvi",
        "symbol": data.symbol.upper(),
        "interval": data.interval,
        "source_type": data.source_type,
        "values": values
    }
    
    
# Positive Volume Index (PVI) 
@app.post("/pvi")
async def get_pvi(data: PVIRequest):
    """Positive Volume Index (PVI)"""
    candles = await fetch_candles(data.symbol, data.interval, data.limit)

    values = calculate_pvi(
        candles=candles,
        source_type=data.source_type,
        sequential=data.sequential
    )

    return {
        "indicator": "pvi",
        "symbol": data.symbol.upper(),
        "interval": data.interval,
        "source_type": data.source_type,
        "values": values
    }


# Ehlers Decycler Oscillator 
@app.post("/dec_osc")
async def get_dec_osc(data: DecOscRequest):
    """Ehlers Decycler Oscillator"""
    candles = await fetch_candles(data.symbol, data.interval, data.limit)

    values = calculate_dec_osc(
        candles=candles,
        hp_period=data.hp_period,
        k=data.k,
        source_type=data.source_type,
        sequential=data.sequential
    )

    return {
        "indicator": "dec_osc",
        "symbol": data.symbol.upper(),
        "interval": data.interval,
        "hp_period": data.hp_period,
        "k": data.k,
        "source_type": data.source_type,
        "values": values
    }


# safezonestop
@app.post("/safezonestop")
async def get_safezonestop(data: SafeZoneStopRequest):
    """safezonestop"""
    candles = await fetch_candles(data.symbol, data.interval, data.limit)

    values = calculate_safezonestop(
        candles=candles,
        period=data.period,
        mult=data.mult,
        max_lookback=data.max_lookback,
        direction=data.direction,
        sequential=data.sequential
    )

    return {
        "indicator": "safezonestop",
        "symbol": data.symbol.upper(),
        "interval": data.interval,
        "params": {
            "period": data.period,
            "mult": data.mult,
            "max_lookback": data.max_lookback,
            "direction": data.direction
        },
        "values": values
    }



# support_resistance_with_breaks
@app.post("/support_resistance_with_breaks")
async def get_support_resistance_with_breaks(data: SupportResistanceBreaksRequest):
    """support_resistance_with_breaks"""
    candles = await fetch_candles(data.symbol, data.interval, data.limit)

    result = calculate_support_resistance_with_breaks(
        candles,
        left_bars=data.left_bars,
        right_bars=data.right_bars,
        vol_threshold=data.vol_threshold
    )

    return {
        "indicator": "support_resistance_with_breaks",
        "symbol": data.symbol,
        "interval": data.interval,
        "params": {
            "left_bars": data.left_bars,
            "right_bars": data.right_bars,
            "vol_threshold": data.vol_threshold
        },
        "values": result
    }



# Time Series Forecast (TSF)
@app.post("/tsf")
async def get_tsf(data: IndicatorWithSourceRequest):
    """Time Series Forecast (TSF)"""
    candles = await fetch_candles(data.symbol, data.interval, data.limit)
    values = calculate_tsf(
        candles=candles,
        period=data.period,
        source_type=data.source_type,
        sequential=data.sequential
    )


    return {
        "indicator": "tsf",
        "symbol": data.symbol.upper(),
        "interval": data.interval,
        "period": data.period,
        "source_type": data.source_type,
        "values": values
    }



# ttm_squeeze (TTM Squeeze)
@app.post("/ttm_squeeze")
async def get_ttm_squeeze(data: TTMSqueezeRequest):
    """# ttm_squeeze (TTM Squeeze)"""
    candles = await fetch_candles(data.symbol, data.interval, data.limit)
    squeeze = calculate_ttm_squeeze(
        candles=candles,
        length_ttms=data.length_ttms,
        bb_mult_ttms=data.bb_mult_ttms,
        kc_mult_low_ttms=data.kc_mult_low_ttms
    )

    return {
        "indicator": "ttm_squeeze",
        "symbol": data.symbol.upper(),
        "interval": data.interval,
        "params": {
            "length_ttms": data.length_ttms,
            "bb_mult_ttms": data.bb_mult_ttms,
            "kc_mult_low_ttms": data.kc_mult_low_ttms,
        },
        "squeeze_detected": squeeze
    }


# Vortex Indicator (VI)
@app.post("/vi")
async def get_vi(data: IndicatorRequest):
    """Vortex Indicator (VI)"""
    candles = await fetch_candles(data.symbol, data.interval, data.limit)
    values = calculate_vi(candles=candles, period=data.period, sequential=data.sequential)

    return {
        "indicator": "vi",
        "symbol": data.symbol.upper(),
        "interval": data.interval,
        "period": data.period,
        "values": values
    }


#  Wavetrend indicator
@app.post("/wt")
async def get_wt(data: WTRequest):
    """Wavetrend indicator"""
    candles = await fetch_candles(data.symbol, data.interval, data.limit)
    values = calculate_wt(
        candles=candles,
        wtchannellen=data.wtchannellen,
        wtaveragelen=data.wtaveragelen,
        wtmalen=data.wtmalen,
        oblevel=data.oblevel,
        oslevel=data.oslevel,
        source_type=data.source_type,
        sequential=data.sequential
    )

    return {
        "indicator": "wt",
        "symbol": data.symbol.upper(),
        "interval": data.interval,
        "values": values
    }


# Stochastic RSI (SRSI)
@app.post("/srsi")
async def get_srsi(data: IndicatorWithSourceRequest):
    """Stochastic RSI (SRSI)"""
    candles = await fetch_candles(data.symbol, data.interval, data.limit)
    values = calculate_srsi(
        candles=candles,
        period=data.period,
        source_type=data.source_type,
        sequential=data.sequential
    )


    return {
        "indicator": "srsi",
        "symbol": data.symbol.upper(),
        "period": data.period,
        "source_type": data.source_type,
        "interval": data.interval, 
        "values": values
    }


# Volume 24h
@app.post("/volume_24h")
async def get_volume_24h(data: Volume24hRequest):
    candles = await fetch_candles(data.symbol, data.interval, data.limit)
    result = calculate_volume_24h(
        candles=candles,
        candles_per_day=data.candles_per_day,
        ma_period=data.ma_period,
        sequential=True
    )

    return {
        "indicator": "volume_24h",
        "symbol": data.symbol.upper(),
        "interval": data.interval,
        "candles_per_day": data.candles_per_day,
        "ma_period": data.ma_period,
        "volume_24h": result["volume_24h"],
        "volume_24h_ma": result["volume_24h_ma"]
    }

