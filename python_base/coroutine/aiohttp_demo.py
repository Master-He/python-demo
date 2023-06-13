import aiohttp  # 第三方包
import asyncio


async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get('https://www.baidu.com/') as response:
            print("Status:", response.status)
            print("Content-type:", response.headers['content-type'])

            html = await response.text()
            print("Body:", html[:15], "...")


asyncio.run(main())
