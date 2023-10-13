import discord

from bot_logic import *



#Переменная intents - хранит привилегии бота
intents = discord.Intents.default()
 #Включаем привелегию на чтение сообщений
intents.message_content = True
 #Создаем бота в переменной client и передаем все привелегии
client = discord.Client(intents=discord.Intents.default())

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send("Hi!")
    elif message.content.startswith('$bye'):
        await message.channel.send("\\U0001f642")
    elif message.content.startswith('$pass'):
        await message.channel.send(gen_pass(10))
    elif message.content.startswith('$emodji'):
        await message.channel.send(gen_emodji())
    else:
        await message.channel.send(message.content)
client.run("MTE1OTg3NzY4NDUwODIzMzc0OQ.Gkl2dr.BlSi3D2LAyHK83q3Z31ZbMagPoEIUHAuxuwd9E")
