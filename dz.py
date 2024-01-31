import requests
import aiohttp
import asyncio
import os
#1
os.mkdir('dz')
for i in range(1,101):
    response=requests.get(f'https://jsonplaceholder.typicode.com/photos/{i}')
    with open(f'./dz/git{i}.json','w') as file:
        file.write(response.text)

#2
os.mkdir('dz_1')

async def download_json(url, session):
    async with session.get(url) as response:
        with open(f"./dz_1/image{url[-1]}.json", 'w') as file:
            file.write(await response.text())
async def save_image():
    urls=[f"https://jsonplaceholder.typicode.com/photos/{i}" for i in range(1,101)]
    async with aiohttp.ClientSession() as session:
        reponse = [download_json(url,session)for url in urls]
        await asyncio.gather(*reponse)
        

if __name__ == '__main__':
    asyncio.run(save_image())
