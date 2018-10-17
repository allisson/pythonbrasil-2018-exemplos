from simple_rest_client.exceptions import ClientError

from simple_rest_client_example.api import get_api_instance

api = get_api_instance()


def get_people():
    for page in range(1, 10):
        people = api.people.list(params={'page': page})
        for p in people.body['results']:
            print(p['name'])


def get_luke():
    luke = api.people.retrieve(1)
    print(luke.body)


def get_404():
    try:
        api.people.retrieve(9999)
    except ClientError as exc:
        print('ClientError, message={}, response={!r}'.format(exc.message, exc.response))


get_people()
get_luke()
get_404()
