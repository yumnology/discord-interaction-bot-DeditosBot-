import discord
from discord.ext import commands
import os
from typing import Union
from discord.ext import commands
from discord.ext.commands import command
from datetime import datetime
import random
import requests
from discord.ext.commands import Bot
from os import getenv
from bs4 import BeautifulSoup
from discord import Client
import asyncio
import time
from collections.abc import Sequence
import praw
from keep_alive import keep_alive
from discord.ext.commands.cooldowns import BucketType

intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix = '+', intents = intents)

#interaction commands set-up
roles = ['introduce el nombre de los roles aqui separados con , y cada rol escrito con ""' ]


#join log set-up
serverid = ('ID del servidor')
channelid = ('ID del canal para logs')


@client.event
async def on_ready():
    print("Ready")
    print (client.user.name)
    await client.change_presence (activity=discord.Activity(type=discord.ActivityType.watching, name="+avatar, +img, +e "))    
#join-log
@client.event
async def on_member_join(member):
  guild = client.get_guild (serverid)
  channel = guild.get_channel(channelid)
  await channel.send(f'📥 {member.mention} (**{member.name}**) se ha unido al servidor, ID: (**{member.id}**), cuenta creada: ``{member.created_at}``')

@client.event
async def on_member_remove(member):
  guild = client.get_guild (serverid)
  channel = guild.get_channel(channelid)
  await channel.send(f'📤 {member.mention} (**{member.name}**) se ha salido del servidor o ha sido kickeado, ID: (**{member.id}**),  cuenta creada:  ``{member.created_at}``')

client.remove_command("help")

#ping command 
@client.command()
async def ping(ctx):
    await ctx.send(f"Pong{round(client.latency*1000)}")

@client.command()
async def pong(ctx):
    await ctx.send(f"Ping{round(client.latency*1000)}")

#avatar command
@commands.has_any_role(*roles)
@commands.guild_only()
@client.command(pass_context=True, aliases=['AVATAR', 'Avatar', 'av', 'ª>ª+ªπ', 'avtar', 'AV', 'aV', 'mirenmifotodeperfilestoybienguapo', 'Av'])
async def avatar(ctx, *, member: discord.Member = None):

    member = ctx.author if not member else member
    embed = discord.Embed(title = f"{member.name}'s avatar", color =  member.color , timestamp= ctx.message.created_at)
    embed.set_image(url=member.avatar_url)  
    await ctx.send(embed=embed)


 #emoji    
@commands.has_any_role(*roles)
@commands.guild_only()
@client.command(pass_context=True, aliases=['E'])
async def e(ctx, emoji: Union[discord.Emoji, discord.PartialEmoji]):
    await ctx.send(emoji.url)

#img command
@commands.has_any_role(*roles)
@client.command(pass_context = True, aliases=['IMG'])
async def img(ctx, *args):
    term = (" ".join(args))
    url = 'https://bing.com/images/search?q=' + term + '&safeSearch=on' + "&FORM=HDRSC2" + '&count=100' + '&mkt=en-US' + '&adlt_set=off'
    USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36 OPR/38.0.2220.41"
    headers = {"user-agent": USER_AGENT}
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, "html.parser")
    count = 0
    linkList = []
    results = soup.find_all('a',class_='iusc')

    for i in results:
        linkList.append(eval(i['m'])['murl'])

    imgEmbed = discord.Embed(title="Image results for "+str(term),  timestamp=datetime.utcnow(), color=0x7A6C6C)
    imgEmbed.set_image(url=linkList[count])
    reacted_message = await ctx.channel.send(embed=imgEmbed)

#interaction
@commands.has_any_role(*roles)
@commands.cooldown(1, 30)
@client.command()
async def hug(ctx, *, member):
    author_name = ctx.message.author.name
    await ctx.send ('**' + (author_name) + '**' + ' ' + 'ha abrazado a' + ' ' + (member) + ' ' + '<a:DeditosHug:847572552011350057>')

@commands.has_any_role(*roles)
@commands.cooldown(1, 10)
@client.command()
async def kiss(ctx, *, member):
    author_name = ctx.message.author.name
    await ctx.send ('**' + (author_name) + '**' + ' ' + 'le da un besito a' + ' ' + (member) + ' ' + '<a:deditoskiss:847583144386756628>')

@commands.has_any_role(*roles)
@commands.cooldown(1, 10)
@client.command()
async def spank(ctx, *, member):
    author_name = ctx.message.author.name
    await ctx.send ('**' + (author_name) + '**' + ' ' + 'le da unas ricas nalgadas a' + ' ' + (member) + ' ' + '<a:deditosspank:847587605317943306>')

@commands.has_any_role(*roles)
@commands.cooldown(1, 30)
@client.command()
async def kick(ctx, *, member):
    author_name = ctx.message.author.name
    await ctx.send ('**' + (author_name) + '**' + ' ' + 'patea a' + ' ' + (member) + ' ' + '<a:deditoskick:847585869610876991>')

@commands.has_any_role(*roles)
@commands.cooldown(1, 30)
@client.command()
async def kill(ctx, *, member):
    author_name = ctx.message.author.name
    await ctx.send ('**' + (author_name) + '**' + ' ' + 'mata a' + ' ' + (member) + ' ' + '<:deditoskill:847591299023634432>')

@commands.has_any_role(*roles)
@commands.cooldown(1, 30)
@client.command()
async def feed(ctx, *, member):
    author_name = ctx.message.author.name
    await ctx.send ('**' + (author_name) + '**' + ' ' + 'le da de comer a' + ' ' + (member) + ' ' + '<:deditosfeed:847593940357611540>')

@commands.has_any_role(*roles)
@commands.cooldown(1, 30)
@client.command()
async def cum(ctx, *, member):
    author_name = ctx.message.author.name
    await ctx.send ('**' + (author_name) + '**' + ' ' + 'eyacula de manera excitante sobre' + ' ' + (member) + ' ' + '<a:deditoscumgif:847890527802490911>')

@commands.has_any_role(*roles)
@commands.cooldown(1, 30)
@client.command()
async def pregnant(ctx, *, member):
    author_name = ctx.message.author.name
    await ctx.send ('**' + (author_name) + '**' + ' ' + 'embaraza de manera fortuita a' + ' ' + (member) + ' ' + '🤰🏻')




keep_alive()

    
client.run(os.getenv('TOKEN'))
