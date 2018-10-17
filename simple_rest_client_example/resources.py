from simple_rest_client.resource import AsyncResource, Resource


def build_actions(resource_name):
    return {
        'list': {
            'method': 'GET',
            'url': resource_name
        },
        'retrieve': {
            'method': 'GET',
            'url': resource_name + '/{}',
        },
        'schema': {
            'method': 'GET',
            'url': resource_name + '/{}',
        },
    }


class PeopleAsyncResource(AsyncResource):
    actions = build_actions('people')


class PeopleResource(Resource):
    actions = build_actions('people')
