from simple_rest_client.api import API

from . import resources


def get_api_instance(api_root_url='https://swapi.co/api/', timeout=5):
    api = API(api_root_url=api_root_url, timeout=timeout)
    api.add_resource(resource_name='people', resource_class=resources.PeopleResource)
    return api


def get_async_api_instance(api_root_url='https://swapi.co/api/', timeout=5):
    api = API(api_root_url=api_root_url, timeout=timeout)
    api.add_resource(resource_name='people', resource_class=resources.PeopleAsyncResource)
    return api
