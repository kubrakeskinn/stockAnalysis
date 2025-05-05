import pytest
from app import create_app, db
from app.models import User, Favorite

@pytest.fixture
def app():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

def test_favorite_crud(client):
    # Ekle
    rv = client.post('/api/favorites', json={'symbol': 'GARAN'})
    assert rv.status_code == 200
    # Listele
    rv = client.get('/api/favorites')
    data = rv.get_json()
    assert any(f['symbol'] == 'GARAN' for f in data)
    # Sil
    rv = client.delete('/api/favorites/GARAN')
    assert rv.status_code == 200 