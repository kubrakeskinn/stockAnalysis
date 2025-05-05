# BIST100 Canlı Takip ve Teknik Analiz Uygulaması

Bu uygulama, BIST100 hisselerini canlı olarak izleyip teknik analiz göstergeleriyle birlikte takip etmenizi sağlar. Kullanıcılar favori sembollerini ekleyebilir, teknik analiz indikatörlerini görebilir ve canlı fiyat güncellemelerini takip edebilir.

## Özellikler
- Canlı BIST100 verisi ve teknik analiz
- Favori sembol ekleme/çıkarma
- Teknik analiz göstergeleri: MA, EMA, RSI, MACD, Bollinger Bands
- Responsive arayüz (Bootstrap 5, Chart.js)
- WebSocket ile canlı güncelleme
- Docker ile kolay kurulum

## Kurulum
1. Depoyu klonlayın ve dizine girin:
   ```bash
   git clone <repo-url>
   cd <proje-dizini>
   ```
2. Sanal ortam oluşturun ve bağımlılıkları yükleyin:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```
3. `.env` dosyasını oluşturun ve API anahtarınızı girin:
   ```bash
   cp .env.example .env
   # .env dosyasını düzenleyin
   ```
4. Uygulamayı başlatın:
   ```bash
   flask run
   # veya
   python -m app
   ```

## Testler
```bash
pytest
```

## Docker ile Çalıştırma
```bash
docker-compose up --build
```

## Yapı
- `app/` - Uygulama kodları
- `app/models.py` - Veritabanı modelleri
- `app/routes.py` - API ve sayfa rotaları
- `app/services/` - Veri ve analiz servisleri
- `app/templates/` - Jinja2 şablonları
- `app/static/` - Statik dosyalar (JS, CSS)
- `tests/` - Testler

## Notlar
- API anahtarınızı `.env` dosyasına eklemeyi unutmayın.
- Teknik analiz için pandas_ta veya TA-Lib kullanılmaktadır. 