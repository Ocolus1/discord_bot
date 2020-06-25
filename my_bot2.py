# my_bot2.py

from discord.ext import commands
import asyncio
from discord.activity import Game
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

client = commands.Bot(command_prefix='/')

@client.event
async def on_ready():
    print("Bot is ready")
    print("Logged in as " + client.user.name)


@client.command()
async def hello(ctx):
    await ctx.send(f'How are you doing?' + ',' + ctx.message.author.mention)


@client.command()
async def dm(ctx):
    await ctx.author.send('How may I help you')


@client.command()
async def square(ctx, num):
    squared_value = int(num) * int(num)
    await ctx.send("The square of " + str(num) + " is " + str(squared_value) + " " + ctx.message.author.mention)


@client.command(name="p")
async def cyrpto(ctx, value):
    symbol = value

    url = f'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest?symbol={symbol}'
    parameters = {
        'start': '1',
        'limit': '5000',
        'convert': 'USD'
    }
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': '2b732aaf-4e57-493e-848f-0c41830e816a',
    }

    session = Session()
    session.headers.update(headers)
    try:
        response = session.get(url)
        datas = response.json()['data'][symbol.upper()]['quote']['USD']
        a, b, *rest = datas
        x = round(datas[a], 2)
        y = round(datas[b], 2)
        await ctx.send(f"""
                        {symbol} {a} : ${x}, \nvolume(24) : ${y}
                        """)
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)


client.run(TOKEN)
