#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import asyncio
from aiohttp import web

from mysql.connector import MySQLConnection, Error
from mysql.connector import errorcode

from tools import config

async def handle_post(request):
    post = await request.json()
    post = json.loads(post)

    name = post['name']
    age = post['age']
    city = post['city']
    
    try:
        params = config()
        conn = MySQLConnection(**params)
        cursor = conn.cursor()
        cursor.callproc('spApp_AddAccount',(str(name),
                                            int(age),                                                         
                                            str(city),                                                    
                                            ))
        conn.commit()
        await asyncio.sleep(10)
        return web.Response(text="Dear {}! Your account data were saved in DB successfuly!".format(name))

    except Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    finally:
        cursor.close()
        conn.close()

app = web.Application()
app.add_routes([web.post('/post', handle_post)])
web.run_app(app)