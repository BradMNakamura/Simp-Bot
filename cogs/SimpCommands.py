import discord
from discord.ext import commands


class SimpCommands(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        await ctx.send('Kiss me on my bolo head')

    @commands.command()
    async def coqui(self, ctx):
        await ctx.send('Check out my SoundCloud dude')
        await ctx.send('https://soundcloud.com/cornelius-clout/coqui')

    @commands.command()
    async def add(self, ctx, numOne, numTwo):
      sum = int(numOne) + int(numTwo)
      if sum > 20 or sum < 0:
        await ctx.send("What the heck dude! I can't count that high!")
      else:
        await ctx.send("That's easy little gamer! It's {0}".format(sum))

def setup(bot):
    bot.add_cog(SimpCommands(bot))
