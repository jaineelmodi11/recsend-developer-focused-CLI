import httpx

class HttpClient:
    def __init__(self, timeout: float = 10.0):
        self.client = httpx.Client(timeout=timeout)

    def request(self, method: str, url: str, headers: dict = None, json=None):
        response = self.client.request(method, url, headers=headers, json=json)
        response.raise_for_status()
        return response
