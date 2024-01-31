import requests
import aiohttp
import asyncio
import os
#1
os.mkdir('dz')
response=requests.get('https://jsonplaceholder.typicode.com/photos/1')
with open('./dz/git.json','w') as file:
    file.write(response.text)

#2
os.mkdir('dz_1')

async def download_json(url, session):
    async with session.get(url) as response:
        with open("./dz_1/image_.json", 'w') as file:
            file.write(await response.text())
async def save_image():
    urls=["https://jsonplaceholder.typicode.com/photos/1"]
    async with aiohttp.ClientSession() as session:
        reponse = [download_json(url,session)for url in urls]
        await asyncio.gather(*reponse)
        

if __name__ == '__main__':
    asyncio.run(save_image())
