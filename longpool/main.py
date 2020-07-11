import asyncio
import traceback

from aiovk.longpoll import BotsLongPoll

from config import *

LONGPOOL_VERSION = int(LONGPOOL_VERSION.replace(".", ""))


class parse(object):

    def __init__(self, r):  # Parsing Pool
        self.lp = r
        self.lp_ts = r["ts"]
        self.lp_updates = r['updates'][0]
        self.lp_type = r['updates'][0]['type']

    async def do(self, mode):
        if mode == "messages":  # Returns only message info
            if LONGPOOL_VERSION >= 5103:
                return self.lp_updates['object']['message']
            else:
                return self.lp_updates['object']

        elif mode == "updates":  # Returns only updates
            return self.lp_updates

        elif mode == "ts":  # Returns only ts
            return self.lp_ts

        return self.lp  # Returns all LongPool


class init:

    def __init__(self,api, group_id: any, mode: str = None):
        self.api = api
        self.group_id = group_id
        self.mode = mode

    async def listen(self):
        print('\nLongpool enabled!')
        while True:
            try:
                lp = BotsLongPoll(self.api, mode=2, group_id=self.group_id)
                while True:
                    r = await lp.wait()
                    if r.get('updates') and r['updates'][0]['type'] == 'message_new' and type == "messages":
                        yield await asyncio.ensure_future(parse(r).do(self.mode))

            except Exception as e:
                print(traceback.format_exc())
