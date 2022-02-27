import discord
from discord import client
from discord import colour
from discord import user
from discord.ext import commands
from discord.member import Member
from discord import Embed
from faker import Faker
import datetime




client = commands.Bot(command_prefix= '/')

@client.event
async def on_ready():
    print("Bot dziala")
    client.load_extension('dismusic')
    client.load_extension('dch')

client.lava_nodes = [
    {
        'host': 'lava.link',
        'port': 80,
        'rest_uri': f'http://lava.link:80',
        'identifier':'MAIN',
        'password':'123',
        'region':'poland',
    }
]




@client.event
async def on_member_join(ctx , member):
    await ctx.send(f'{member} dołączył na server!')
@client.event
async def on_member_remove(ctx , member):
      await ctx.send(f"{member} wyszedł z server'a")

@client.command(alisases = ["names" , "imiona"])
async def Names(ctx):
    fake = Faker()
    for _ in range (5):
        await ctx.send(fake.name())


@client.command(aliases=["wyczysc" , "clear"])
@commands.has_permissions(administrator=True)
async def Clear(ctx , amount = 1 ):
    await ctx.message.delete()
    await ctx.channel.purge(limit=amount + 1)
    await ctx.send(f'{amount} wiadomosci zostalo usunięte!')


@client.command(aliases = ["Time", "Czas"])
async def _(ctx):
        CurrentTime = datetime.datetime.today().replace(microsecond=0)
        await ctx.send(f"Current time: {CurrentTime}")


    

@client.command(aliases=["kick", "wyrzuc"])
@commands.has_permissions(administrator=True)
async def Kick(ctx , member: discord.Member, * , reason =None):
    await member.ban(reason = reason)
    await ctx.send(f'{member}  został zbanowany przez {ctx.message.author}' )

@client.command(aliases=["unban"])
@commands.has_permissions(administrator=True)
async def Unban(ctx, member: discord.Member):
    guild = ctx.guild
    embed = discord.Embed(
        title = "Unbaned!",
        description = (f'{member} został odbanowany przez {ctx.message.author}')
    )
    if ctx.author.guild_permissions.ban_members:
        await ctx.send(embed = embed)
        await guild.unban(user = user)

@client.command(aliases=["info", "id"])
@commands.has_permissions(administrator=True)
async def Info(ctx, member: discord.Member ):
    embed = discord.Embed(title= member.display_name , description = member.mention, color = discord.Color.red()) 
    embed.add_field(name = "ID" , value = member.id , inline=True)
    embed.set_thumbnail(url = member.avatar_url)
    embed.set_author(name = member.display_name)
    await ctx.send(embed=embed)


client.run()
