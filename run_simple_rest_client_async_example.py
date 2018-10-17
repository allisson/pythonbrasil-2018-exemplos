import asyncio

from simple_rest_client.exceptions import ClientError

from simple_rest_client_example.api import get_async_api_instance

api = get_async_api_instance()


async def _get_people(page):
    people = await api.people.list(params={'page': page})
    for p in people.body['results']:
        print(p['name'])


async def get_people():
    tasks = [_get_people(page) for page in range(1, 10)]
    await asyncio.gather(*tasks)


async def get_luke():
    luke = await api.people.retrieve(1)
    print(luke.body)


async def get_404():
    try:
        await api.people.retrieve(9999)
    except ClientError as exc:
        print('ClientError, message={}, response={!r}'.format(exc.message, exc.response))


async def main():
    # await asyncio.gather(get_people(), get_luke(), get_404())
    await get_people()
    await get_luke()
    await get_404()


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
