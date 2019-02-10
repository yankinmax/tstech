#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import aiohttp
import asyncio
import json
import sys
import functools

class Prompt:
    def __init__(self, loop=None):
        self.loop = loop or asyncio.get_event_loop()
        self.q = asyncio.Queue(loop=self.loop)
        self.loop.add_reader(sys.stdin, self.got_input)

    def got_input(self):
        asyncio.ensure_future(self.q.put(sys.stdin.readline()), loop=self.loop)

    async def __call__(self, msg, end='\n', flush=False):
        print(msg, end=end, flush=flush)
        return (await self.q.get()).rstrip('\n')

prompt = Prompt()
raw_input = functools.partial(prompt, end='', flush=True)

async def input():
    # simulate raw_input
    name = await raw_input('enter name:')
    age = await raw_input('enter age:')
    city = await raw_input('enter city:')
    return name, age, city

loop = asyncio.get_event_loop()
name, age, city = loop.run_until_complete(input())

account = {
	"name": name,
	"age": age,
	"city": city,
}

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

async def main():
    async with aiohttp.ClientSession() as session:
        async with session.post('http://192.168.1.227:8080/post', json=json.dumps(account)) as resp: 	
	        print(await resp.text())

loop.run_until_complete(main())