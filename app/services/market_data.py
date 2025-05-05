import os
import requests
import time
from dotenv import load_dotenv
from functools import lru_cache

load_dotenv()
API_KEY = os.getenv('API_KEY')
API_PROVIDER = os.getenv('API_PROVIDER', 'finnhub')

_cache = {}
_cache_time = {}

BIST100_SYMBOLS = ["GARAN", "AKBNK", "THYAO", "SISE", "KRDMD", "ISCTR", "ASELS", "BIMAS", "FROTO", "TUPRS"]

def _fetch_from_api(symbol):
    # Gerçek API entegrasyonu için burası değiştirilecek
    # Örnek: Finnhub
    url = f"https://finnhub.io/api/v1/quote?symbol={symbol}.IS&token={API_KEY}"
    r = requests.get(url)
    if r.status_code == 200:
        data = r.json()
        return {
            'symbol': symbol,
            'price': data.get('c'),
            'open': data.get('o'),
            'high': data.get('h'),
            'low': data.get('l'),
            'prev_close': data.get('pc'),
            'volume': data.get('v'),
            'change_percent': ((data.get('c')-data.get('pc'))/data.get('pc'))*100 if data.get('pc') else 0
        }
    return None

def get_live_quote(symbol):
    now = time.time()
    if symbol in _cache and now - _cache_time[symbol] < 30:
        return _cache[symbol]
    data = _fetch_from_api(symbol)
    _cache[symbol] = data
    _cache_time[symbol] = now
    return data

def get_live_quote_with_ta(symbol):
    data = get_live_quote(symbol)
    # Burada geçmiş OHLC ve TA hesaplaması eklenecek
    # Şimdilik sadece fiyat verisi dönüyor
    return data 