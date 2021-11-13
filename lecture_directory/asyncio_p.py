import asyncio
import time

async def waiter(n):
    await asyncio.sleep(n)
    print("waited for {} second".format(n))


# async def main():
#     # Event Loop
#     task1 = asyncio.create_task(waiter(4))
#     task2 = asyncio.create_task(waiter(2))
#     print(time.strftime('%X'))
#     await task1  # await means completion of the task --> run this task to completion
#     await task2
#     await asyncio.sleep(5)  # Now even if the above tasks get completed early, the program will exit after 5 second only
#     print(time.strftime('%X'))

# result with above piece of code -->
    # 21:22:49
    # waited for 2 second
    # waited for 4 second
    # 21:22:53
async def main():
    # Event Loop
    task1 = asyncio.create_task(waiter(2))
    task2 = asyncio.create_task(waiter(3))
    print(time.strftime('%X'))
    # await task1  # await means completion of the task --> run this task to completion
    # await task2
    await asyncio.sleep(3)
    print(time.strftime('%X'))


if __name__ == "__main__":
    asyncio.run(main())


# download files asynchronously
import aiohttp
