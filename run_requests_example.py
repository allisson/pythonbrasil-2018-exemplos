from requests_example.api import API
from requests_example.exceptions import ClientError

api = API()


def get_people():
    for page in range(1, 10):
        people = api.people(page=page)
        for p in people['results']:
            print(p['name'])


def get_luke():
    luke = api.people_detail(1)
    print(luke)


def get_404():
    try:
        api.people_detail(9999)
    except ClientError as exc:
        response = exc.args[0]
        print('ClientError, status_code={}, content={}'.format(response.status_code, response.text))


get_people()
get_luke()
get_404()
