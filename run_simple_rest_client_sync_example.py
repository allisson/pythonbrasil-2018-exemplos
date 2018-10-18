from simple_rest_client.exceptions import ClientError

from simple_rest_client_example.api import get_api_instance

api = get_api_instance()


def get_people():
    for page in range(1, 10):
        response = api.people.list(params={'page': page})
        for p in response.body['results']:
            print(p['name'])


def get_luke():
    response = api.people.retrieve(1)
    print(response.body)


def get_404():
    try:
        api.people.retrieve(9999)
    except ClientError as exc:
        print('ClientError, message={}, response={!r}'.format(exc.message, exc.response))


get_people()
get_luke()
get_404()
