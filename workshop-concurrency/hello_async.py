import asyncio


async def hello():
    print('Hello')
    await asyncio.sleep(3)
    print('World')


async def main():
    await asyncio.gather(hello(), hello(), hello())

if __name__ == '__main__':
    import time
    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter()
    print(f"{__file__} executed in  {elapsed:0.2f} seconds.")
