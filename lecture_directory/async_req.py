import asyncio
import aiohttp
import time


async def fetch_from_google():
    url = "https://www.google.com"
    session = aiohttp.ClientSession()
    resp = await session.get(url)
    async with open("file.txt","w") as file:
        await resp.content.read(256)
    await session.close()


async def main():
    print(time.strftime('%X'))
    await asyncio.gather(
        fetch_from_google(),
        fetch_from_google(),
        fetch_from_google(),
        fetch_from_google(),
        fetch_from_google(),
        fetch_from_google(),
        fetch_from_google(),
        fetch_from_google(),
        fetch_from_google(),
        fetch_from_google(),
        fetch_from_google(),
        fetch_from_google()
        # or
        # *[
        #     fetch_from_google() for _ in range(20)
        #   ]
     )
    print(time.strftime('%X'))

if __name__ == "__main__":
    asyncio.run(main())
