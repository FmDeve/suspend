import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time


Client = discord.Client() 
client = commands.Bot(command_prefix = "!") 
#Subways Bot

chat_filter = ["Fuck", "Shit", "Ass", "fuck", "nigg", "fuk", "cunt", "cnut", "bitch", "dick", "d1ck", "pussy," "asshole", "b1tch", "b!tch", "blowjob", "cock", "c0ck"]
bypass_list = []


@client.event 
async def on_ready():
    print("Bot is online and connected to Discord") 

@client.event
async def on_message(message):
    if message.content == "cookie":
        await client.send_message(message.channel, ":cookie:")
    if message.content.upper().startswith('!EMBED'):
        if "498510048541278220" in [role.id for role in message.author.roles]:
            args = message.content.split(" ")
            embed = discord.Embed(colour=0xE9A72F)
            embed.add_field(name="%s" % (" ".join(args[1:])), value="Made by Fm_Developer#4182")
            await client.send_message(message.channel, embed=embed)
        else:
            await client.send_message(message.channel, "You do not have permission")
    if message.content.upper().startswith('!AMIADMIN'):
        if "498510048541278220" in [role.id for role in message.author.roles]: 
            await client.send_message(message.channel, "You are an admin")
        else:
            await client.send_message(message.channel, "You are not an admin")
    if message.content.upper().startswith('!SAY'):
        if "498510048541278220" in [role.id for role in message.author.roles]:
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
                    await client.send_message(message.channel, "**Hey!** You're not allowed to use that word here!")
                except discord.errors.NotFound:
                    return
    if message.content.upper().startswith('!BAN'):
        if "498510048541278220" in [role.id for role in message.author.roles]:
            args = message.content.split(" ")
            member = discord.utils.get(message.server.members, mention=args[1])
            await client.send_message(member, "You Have Been Banned From Subway")
            await client.ban(member)
        else:
            await client.send_message(message.channel, "You are not an Admin")
    if message.content.upper().startswith('!KICK'):
        if "498510048541278220" in [role.id for role in message.author.roles]:
            args = message.content.split(" ")
            member = discord.utils.get(message.server.members, mention=args[1])
            await client.send_message(member, "You Have Been Kicked From Subway")
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
            embed.add_field(name="**Command List** \n `!bannedwords` - *Sends the banned word list* \n `!kick` - *Kicks the specified user from the discord* \n `!ban` - *Bans the specified user from the discord* \n `!warn`- *warns the user you specify* ", value="Made by Fm_Developer#4182")
            await client.send_message(message.channel, embed=embed)
    if mesage.content.upper().startswith('!WARN'):
        if "498510048541278220" in [role.id for role in message.author.roles]:
            args = message.content.split(" ")
            member = discord.utils.get(message.server.members, mention=args[1])
            await client.send.message(member, "You have been warned in Subway for:" "%s" % (" ").join(args[2:]))
            await client.send.message(message.get_channel("124323"), member "Has been warned for:", "s%" % (" ").join(args[2:])))
        else:
            await client.send_message(message.channel, "You are not an Admin")
client.run("NDk4NTA3NDg1MzM5MDU4MTk2.Dpuwdw.j7Wgqwk9P7N9AjI7tFynUZ49psc")


 
