import asyncio
import aiovk
import longpool
from config import *

aiovk.TokenSession.API_VERSION = "5.120" # Edit vk api version in lib

api = aiovk.API(aiovk.TokenSession(access_token=VK_TOKEN)) # Authorize with token
longpool = longpool.init(api, GROUP_ID, "messages") # or longpool = longpool.init(api, GROUP_ID, {mode})
bot_loop = asyncio.get_event_loop()

async def info(data):
    print(f'\nMessage from: {data["from_id"]}\nPeer_id: {data["peer_id"]}\nText: {data["text"]}')

async def start():

    async for messages in longpool.listen(): # Listen longpool
        await info(messages)

if __name__ == '__main__':
    try:
        bot_loop.run_until_complete(start())
    except KeyboardInterrupt:
        print('\nExiting...')
        exit(0)