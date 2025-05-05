from flask import Blueprint, request, jsonify, render_template
from .models import db, User, Favorite
from .services.market_data import get_live_quote_with_ta
from .services.ta import get_ta_indicators

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/api/favorites', methods=['GET'])
def get_favorites():
    user = User.query.first()
    if not user:
        user = User()
        db.session.add(user)
        db.session.commit()
    favorites = Favorite.query.filter_by(user_id=user.id).all()
    result = []
    for fav in favorites:
        data = get_live_quote_with_ta(fav.symbol)
        result.append({
            'symbol': fav.symbol,
            'added_at': fav.added_at,
            'data': data
        })
    return jsonify(result)

@main.route('/api/favorites', methods=['POST'])
def add_favorite():
    symbol = request.json.get('symbol')
    user = User.query.first()
    if not user:
        user = User()
        db.session.add(user)
        db.session.commit()
    if not Favorite.query.filter_by(user_id=user.id, symbol=symbol).first():
        fav = Favorite(symbol=symbol, user_id=user.id)
        db.session.add(fav)
        db.session.commit()
    return jsonify({'status': 'ok'})

@main.route('/api/favorites/<symbol>', methods=['DELETE'])
def delete_favorite(symbol):
    user = User.query.first()
    fav = Favorite.query.filter_by(user_id=user.id, symbol=symbol).first()
    if fav:
        db.session.delete(fav)
        db.session.commit()
    return jsonify({'status': 'deleted'})

@main.route('/api/quote/<symbol>', methods=['GET'])
def get_quote(symbol):
    data = get_live_quote_with_ta(symbol)
    return jsonify(data) 