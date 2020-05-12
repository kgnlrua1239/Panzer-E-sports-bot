import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("Panzer E-sports")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    if message.content.startswith("펜저야 뭐해"):
        await message.channel.send('네 생각')

    if message.content.startswith("펜저야 자니"):
        await message.channel.send('ㅇㅇ')


access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
