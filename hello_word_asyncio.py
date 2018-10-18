import asyncio

import aiohttp


async def get_people(session):
    url = 'https://swapi.co/api/people/'
    async with session.get(url) as response:
        people = await response.json()
        for person in people['results']:
            print(person['name'])


async def main():
    async with aiohttp.ClientSession() as session:
        await get_people(session)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
