import os
import requests as r
from'telegraph'import upload_file
from pyrogram import *
from pyrogram.types import *
from pyrogram.enums import *

#NAME => YOUR BOTS FILE NAME
from NAME import pbot

#ADD ANY BUTTON YOU WANT BELOW YOUR WELCOME IMAGE
markup=InlineKeyboardMarkup ([[InlineKeyboardButton ("MODS", url="https://t.me/NovaXMod")]])

@pbot.on_message(filters.new_chat_members & filters.group)
async def welcomepic(_, message):

    for u in message.new_chat_members:
        MSG = f"""
**WELCOME TO {message.chat.title}
âž–âž–âž–âž–âž–âž–âž–âž–âž–âž–âž–âž–
NAME: {u.mention}
ID: {u.id}
USERNAME: @{u.username}
COUNT: {await pbot.get_chat_members_count(message.chat.id)}
âž–âž–âž–âž–âž–âž–âž–âž–âž–âž–âž–âž–**
"""

        uid = u.id
        try:
            Up = (await pbot.get_chat(uid)).photo
            
            await pbot.download_media(Up.big_file_id, file_name=f"pfp_{uid}.png")
            
            a = upload_file(f"./downloads/pfp_{uid}.png")

            for x in a:
                url = "https://graph.org/" + x
                resp = r.post("https://novax-api-7c5f1d45a2f2.herokuapp.com/generate", json={'name' : f'{u.first_name}','user_name' : f'@{u.username}','user_id' : f'{u.id}','profile_pic' : f'{url}','group_name' : f'{message.chat.title}' ,"auth_key" : "Yash_Yash__@"}).json()
                await message.reply_photo((resp['image_url']), caption=MSG, reply_markup=markup)
                os.remove(f"./downloads/pfp_{uid}.png")
        except AttributeError:
            resp = r.post("https://novax-api-7c5f1d45a2f2.herokuapp.com/generate", json={'name' : f'{u.first_name}','user_name' : f'@{u.username}','user_id' : f'{u.id}','group_name' : f'{message.chat.title}' ,"auth_key" : "Yash_Yash__@"}).json()
            await message.reply_photo((resp['image_url']), caption=MSG, reply_markup=markup)
            os.remove(f"./downloads/pfp_{uid}.png")
