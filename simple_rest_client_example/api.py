from simple_rest_client.api import API

from . import resources


def get_api_instance(api_root_url='https://swapi.co/api/', timeout=5):
    api = API(api_root_url=api_root_url, timeout=timeout)
    api.add_resource(resource_name='films', resource_class=resources.FilmsResource)
    api.add_resource(resource_name='people', resource_class=resources.PeopleResource)
    api.add_resource(resource_name='planets', resource_class=resources.PlanetsResource)
    api.add_resource(resource_name='species', resource_class=resources.SpeciesResource)
    api.add_resource(resource_name='starships', resource_class=resources.StarshipsResource)
    api.add_resource(resource_name='vehicles', resource_class=resources.VehiclesResource)
    return api


def get_async_api_instance(api_root_url='https://swapi.co/api/', timeout=5):
    api = API(api_root_url=api_root_url, timeout=timeout)
    api.add_resource(resource_name='films', resource_class=resources.FilmsAsyncResource)
    api.add_resource(resource_name='people', resource_class=resources.PeopleAsyncResource)
    api.add_resource(resource_name='planets', resource_class=resources.PlanetsAsyncResource)
    api.add_resource(resource_name='species', resource_class=resources.SpeciesAsyncResource)
    api.add_resource(resource_name='starships', resource_class=resources.StarshipsAsyncResource)
    api.add_resource(resource_name='vehicles', resource_class=resources.VehiclesAsyncResource)
    return api
