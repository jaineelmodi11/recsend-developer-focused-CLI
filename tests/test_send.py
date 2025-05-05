import respx
import pytest
from recsend.utils.http_client import HttpClient

@respx.mock
def test_http_client_request():
    url = "https://example.com/test"
    route = respx.post(url).respond(
        status_code=200,
        json={"ok": True},
        headers={"Content-Type": "application/json"}
    )

    client = HttpClient()
    response = client.request("POST", url, headers={}, json={"foo": "bar"})

    assert route.called
    assert response.status_code == 200
    assert response.json() == {"ok": True}
