from simple_rest_client.resource import AsyncResource, Resource


films_actions = {
    'list': {
        'method': 'GET',
        'url': 'films'
    },
    'retrieve': {
        'method': 'GET',
        'url': 'films/{}',
    },
    'schema': {
        'method': 'GET',
        'url': 'films/schema',
    },
}

people_actions = {
    'list': {
        'method': 'GET',
        'url': 'people'
    },
    'retrieve': {
        'method': 'GET',
        'url': 'people/{}',
    },
    'schema': {
        'method': 'GET',
        'url': 'people/schema',
    },
}

planets_actions = {
    'list': {
        'method': 'GET',
        'url': 'planets'
    },
    'retrieve': {
        'method': 'GET',
        'url': 'planets/{}',
    },
    'schema': {
        'method': 'GET',
        'url': 'planets/schema',
    },
}

species_actions = {
    'list': {
        'method': 'GET',
        'url': 'species'
    },
    'retrieve': {
        'method': 'GET',
        'url': 'species/{}',
    },
    'schema': {
        'method': 'GET',
        'url': 'species/schema',
    },
}

starships_actions = {
    'list': {
        'method': 'GET',
        'url': 'starships'
    },
    'retrieve': {
        'method': 'GET',
        'url': 'starships/{}',
    },
    'schema': {
        'method': 'GET',
        'url': 'starships/schema',
    },
}

vehicles_actions = {
    'list': {
        'method': 'GET',
        'url': 'vehicles'
    },
    'retrieve': {
        'method': 'GET',
        'url': 'vehicles/{}',
    },
    'schema': {
        'method': 'GET',
        'url': 'vehicles/schema',
    },
}


class FilmsAsyncResource(AsyncResource):
    actions = films_actions


class FilmsResource(Resource):
    actions = films_actions


class PeopleAsyncResource(AsyncResource):
    actions = people_actions


class PeopleResource(Resource):
    actions = people_actions


class PlanetsAsyncResource(AsyncResource):
    actions = planets_actions


class PlanetsResource(Resource):
    actions = planets_actions


class SpeciesAsyncResource(AsyncResource):
    actions = species_actions


class SpeciesResource(Resource):
    actions = species_actions


class StarshipsAsyncResource(AsyncResource):
    actions = starships_actions


class StarshipsResource(Resource):
    actions = starships_actions


class VehiclesAsyncResource(AsyncResource):
    actions = vehicles_actions


class VehiclesResource(Resource):
    actions = vehicles_actions
