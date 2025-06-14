import backend.app as app

def test_queue_endpoint():
    client = app.app.test_client()
    resp = client.get('/api/queue')
    assert resp.status_code == 200
