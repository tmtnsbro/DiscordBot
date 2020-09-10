import discord
import random

from discord.ext import commands

client = commands.Bot(command_prefix='.')

@client.event
async def on_ready():
        print('Logged on as TMTNSBRO#1995')


@client.command()
async def ping(ctx):
    await ctx.send(f'{round(client.latency * 1000)}ms')

@client.command()
async  def drop(ctx):
    responses = ['Dusty Depot',
                 'Flush Factory',
                 'Lama Depot']
    await ctx.author.send((random.choice(responses)))

@client.command()
async def start(ctx):
    await ctx.send('Ok, started check your DMs and continue from there!')
    await ctx.author.send ('Ok, We will start from here. Please do not write .start again, it '
                           'might mess your account up with this bot. Start with .help to list '
                           'all of the available commands. ')



client.run('NzUyMzc1NTU0Mzg0MzMwODQ0.X1WuVg.9pInn1pL_nleICImaWuWiJ9mTUo')
