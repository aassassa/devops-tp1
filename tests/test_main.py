from app.main import app

def test_home():
    client = app.test_client()
    r = client.get('/')
    assert r.status_code == 200
    assert r.json['status'] == 'running'

def test_hello():
    client = app.test_client()
    r = client.get('/hello/Mohamed')
    assert r.status_code == 200
    assert r.json['message'] == 'Bonjour Mohamed !'