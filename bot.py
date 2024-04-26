import asyncio
from pyrogram import Client, compose,idle
import os

from plugins.cb_data import app as Client2

TOKEN = os.environ.get("TOKEN", "7103264571:AAHQABT_b98LJ_tklhwsTLSaPU6OibhTocE")

API_ID = int(os.environ.get("API_ID", "27972068"))

API_HASH = os.environ.get("API_HASH", "6e7e2f5cdddba536b8e603b3155223c1")

STRING = os.environ.get("STRING", "")



bot = Client(

           "Renamer",

           bot_token=TOKEN,

           api_id=API_ID,

           api_hash=API_HASH,

           plugins=dict(root='plugins'))
           

if STRING:
    apps = [Client2,bot]
    for app in apps:
        app.start()
    idle()
    for app in apps:
        app.stop()
    
else:
    bot.run()
