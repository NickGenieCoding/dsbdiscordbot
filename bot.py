import discord
import pydsb 
import os
from html2image import Html2Image

client = discord.Client()
dsb = pydsb.PyDSB("DSB-Username", "DSB-Password") #Insert your DSB Username and Password here
hti = Html2Image()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$plan'): #To get to plan in Discord, type: $plan
        plan = dsb.get_plans()
        s1 = plan[1]
        s2 = plan[2]
        url1 = s1['url']
        url2 = s2['url'] 
        hti.screenshot(url= url1, save_as='1.png', size=(1000, 1800))
        await message.channel.send(file= discord.File('1.png')) 
        hti.screenshot(url= url2, save_as='2.png', size=(1000, 1800))
        await message.channel.send(file= discord.File('2.png'))
        os.remove("1.png")
        os.remove("2.png")



client.run('DiscordBotToken') #Insert your DiscordBot-Token here