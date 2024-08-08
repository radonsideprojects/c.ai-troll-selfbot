import json
import discord
from discord.ext import commands
from characterai import aiocai

char = "" # Your c.ai character

with open('config.json', 'r') as file:
    config = json.loads(file.read())
    token = config['discord']
    cai = config['cai']

bot = commands.Bot(command_prefix=",", self_bot=True)
client = aiocai.Client(cai)

doRespond = True
room = None
chat = None

@bot.event
async def on_ready():
    global room
    global chat
    me = await client.get_me()
    chat = await client.connect()
    room, _ = await chat.new_chat(char, me.id)

@bot.event
async def on_message(message):
    global chat
    global room
    global doRespond
    if doRespond:
        if bot.user.mentioned_in(message):
            if message.author.id != 1222859629394919444:
                try:
                    me = await client.get_me()
                    responce = await chat.send_message(char, room.chat_id, message.content  + f" | OOC: This message was sent by: {message.author.name}")
                    await message.reply(responce.text)
                except:
                    pass
            doRespond = True

    await bot.process_commands(message)
    
bot.run(token)
