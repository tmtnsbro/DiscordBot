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
async  def drop(ctx, *, questions):
    responses = ['Dusty Depot',
                 'Flush Factory',
                 'Lama Depot']
    await ctx.send(f'Question: {questions}\nAnswer: {random.choice(responses)}')

client.run('NzUyMzc1NTU0Mzg0MzMwODQ0.X1WuVg.zP_-wh1AI6fy-5N3WlosHM7YNSs')
