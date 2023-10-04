def test_healthcheck_when_request_receiving_ok(test_app):
    response = test_app.get("/health-check")

    assert response.status_code == 200
    assert response.json() == {"msg": "Application running"}
