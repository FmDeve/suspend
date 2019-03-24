import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time

Client = discord.Client() 
client = commands.Bot(command_prefix = "!") 
#Nub Army

chat_filter = ["APPLE"]
bypass_list = []


@client.event 
async def on_ready():
    print("Bot is online and connected to Discord")
    await client.send_message(discord.Object(id='558128313009176579'),  "***Bot Restarted!***")

@client.event
async def on_message(message):
    if message.content == "cookie":
        await client.send_message(message.channel, ":cookie:")
    if message.content == "ping":
        embed = discord.Embed(colour=0x0dc93f)
        embed.add_field(name=":timer: Pong!", value="Made by Fm_Developer#4182")
        await client.send_message(message.channel, embed=embed)
    if message.content.upper().startswith('!EMBED'):
        if "558141576770093056" in [role.id for role in message.author.roles]:
            args = message.content.split(" ")
            embed = discord.Embed(colour=0xE9A72F)
            embed.add_field(name="%s" % (" ".join(args[1:])), value="*Bot made by Fm_Developer*")
            await client.send_message(discord.Object(id='559050683979005983559050683979005983'),  embed=embed)
        else:
            await client.send_message(message.channel, "You do not have permission")
    if message.content.upper().startswith('!AMIADMIN'):
        if "558141576770093056" in [role.id for role in message.author.roles]: 
            await client.send_message(message.channel, "You are an admin")
        else:
            await client.send_message(message.channel, "You are not an admin")
    if message.content.upper().startswith('!SAY'):
        if "558141576770093056" in [role.id for role in message.author.roles]:
            args = message.content.split(" ")
            await client.send_message(message.channel, "%s" % (" ".join(args[1:])))
        else:
            await client.send_message(message.channel, "You do not have permission")
    contents = message.content.split(" ") 
    for word in contents:
        if word.upper() in chat_filter:
            if not message.author.id in bypass_list:
                try:
                    await client.delete_message(message)
                    await client.send_message(message.channel, "Stop saying bad words. Your not cool (:icecream:) so stop it. :octagonal_sign:")
                except discord.errors.NotFound:
                    return
    if message.content.upper().startswith('!BAN'):
        if "558141576770093056" in [role.id for role in message.author.roles]:
            args = message.content.split(" ")
            member = discord.utils.get(message.server.members, mention=args[1])
            await client.send_message(member, "You Have Been Banned From Nub Army")
            await client.ban(member)
        else:
            await client.send_message(message.channel, "You are not an Admin")
    if message.content.upper().startswith('!KICK'):
        if "558141576770093056" in [role.id for role in message.author.roles]:
            args = message.content.split(" ")
            member = discord.utils.get(message.server.members, mention=args[1])
            await client.send_message(member, "You Have Been Kicked From Nub Army")
            await asyncio.sleep(2)
            await client.kick(member)
        else:
            await client.send_message(message.channel, "You are not an Admin")
    if message.content == "!cmds":
        embed = discord.Embed(colour=0xE9A72F)
        embed.add_field(name="**Command List** \n `cookie` - *Gives you a cookie* \n `!say` - *Makes the bot say whatever you want* \n `!embed` - *Creats a announcement* \n `!amIadmin` - *tells you your moderation Status* \n `!cmds2` - *Displays the second list of commands*", value="Made by Fm_Developer#4182")
        await client.send_message(message.channel, embed=embed)
    if message.content.upper().startswith('!CMDS2'):
            embed = discord.Embed(colour=0xE9A72F)
            embed.add_field(name="**Command List** \n `!kick` - *Kicks the specified user from the discord* \n `!ban` - *Bans the specified user from the discord* \n `!warn`- *warns the user you specify* ", value="Made by Fm_Developer#4182")
            await client.send_message(message.channel, embed=embed)
    if message.content == "!bannedwordlist":
        await client.send_message(message.channel, "Why do you wanna look at innapropriate words? Huh? I am on to you.")



            
client.run('NTU5MjA4ODg5ODY3MDQyODQ3.D3iDcA.Uak5HcHGmJaroWCc-m2JOr5wW00')


#hex codes -- red- 0xca054d, orange - 0xff7f50, yellow - 0xfbfd3e, green - 0x0dc93f, blue - 0x00e4f6, purple - 0x610083 , magenta - 0xef00ef
