import nextcord
from nextcord import Interaction
from nextcord.ext import commands

TOKEN = 'MTAxMDc1MDg1OTY5NDU4Mzg4OQ.GvGsTR.9sumzDq8c8zBMKocrQavfx887G8790SiZOOL3w'

intents = nextcord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix = '!', intents=intents)

@client.event
async def on_ready():
    print('Bot {} telah online'.format(client.user))
    
@client.command()
async def hello(ctx):
    await ctx.send('Hello, {}! Semuanya'.format(ctx.author.name.title()))
    
bot.run(TOKEN)