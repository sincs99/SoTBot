import json
import discord
import io
import aiohttp
import urllib.request, json

with urllib.request.urlopen("https://sotdrop.herokuapp.com/results") as url:
    data = json.loads(url.read().decode())
from discord.ext import commands
from discord.ext import tasks

bot = commands.Bot(command_prefix='/')

import requests as requests


class MyClient(discord.Client):
    async def on_ready(self):
        print("Logged in")

    async def on_message(self, message):

        if message.author == client.user:
            return

        if message.content.startswith("/drop"):
            print(data)
            await message.channel.send(data)

        if message.content.startswith("/help"):
            await message.reply(
                '```Info \n /island (island name) - Sends infos about the requested island \n … For my code blocks!```')

        if message.content.startswith("/island "):
            isle = message.content.split(' ')[1]
            print(isle)

            if isle.lower() == "crooks":
                await message.channel.send(file=discord.File('img/crook.jpg'))
            if isle.lower() == "thieves":
                await message.channel.send("file=discord.File('img/crook.jpg')")
            if isle.lower() == "plunder":
                embed = discord.Embed(
                    color=discord.Colour.dark_gray()
                )
                embed.add_field(name='If you wish to add me in your server,',
                                value='https://seaofthieves.fandom.com/wiki/Plunder_Valley', inline=False)
                await message.channel.send(embed=embed)


client = MyClient()

"""
Change token !!

"""


client.run("")
