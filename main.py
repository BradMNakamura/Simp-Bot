import os
from discord.ext import commands
client = commands.Bot(command_prefix='?')

@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

@client.event
async def on_ready():
  print('The bot is online')
  for filename in os.listdir('./cogs'):
      if filename.endswith('.py'):
          client.load_extension(f'cogs.{filename[:-3]}')

client.run('NzMwMzEwNjE1OTY4Nzc2MjIz.XwVoww.tFYMxBmz5mAAmyqMthhTJ_AEeXU')
