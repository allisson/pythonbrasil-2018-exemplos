import requests
import status
from requests.exceptions import ConnectionError, Timeout

from .exceptions import ClientConnectionError, ClientError, ServerError


class API:
    def __init__(self, timeout=5):
        self.api_root_url = 'https://swapi.co/api'
        self.session = requests.Session()
        self.timeout = timeout

    def _make_request(self, method, url, **kwargs):
        request_method = getattr(self.session, method.lower())

        try:
            response = request_method(url, timeout=self.timeout, **kwargs)
        except (ConnectionError, Timeout) as exc:
            raise ClientConnectionError(exc)

        if status.is_client_error(code=response.status_code):
            raise ClientError(response)

        if status.is_server_error(code=response.status_code):
            raise ServerError(response)

        return response

    def people(self, page=1):
        url = '{}/people/'.format(self.api_root_url)
        params = {'page': page}
        response = self._make_request('GET', url, params=params)
        return response.json()

    def people_detail(self, pk):
        url = '{}/people/{}/'.format(self.api_root_url, pk)
        response = self._make_request('GET', url)
        return response.json()
