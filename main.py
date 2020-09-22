import discord
from discord.ext import commands
import asyncio
from image import get_gif, get_image
import random
from pathlib import Path

data_folder = Path("files/")

MONKE_BOT_ID = "<@!757075376148185089>"

DISCORD_TOKEN = open(data_folder / "token.txt", "r").readline()

screech_sounds = [data_folder / "screech_loud.mp3", data_folder / "screech.mp3"]

with open(data_folder / "8ball_responses.txt") as f:
    _8ball_responses = [line.rstrip() for line in f]

with open(data_folder / "shooting_gif.txt") as f:
    shooting_gifs = [line.rstrip() for line in f]

with open(data_folder / "monkey_facts.txt") as f:
    monkey_facts = [line.rstrip() for line in f]

client = commands.Bot(command_prefix='.monke ')

random.seed()


@client.command(aliases=['Pog'])
async def pog(ctx):
    queries = ["spider monkey mouth open", "monkey open mouth", "howler monkey mouth"]
    link = get_image(queries, 10)
    await ctx.send(link)


@client.command()
async def connect(ctx, *, channel: discord.VoiceChannel = None):
    if not channel:
        try:
            channel = ctx.author.voice.channel
        except AttributeError:
            await ctx.send(f':see_no_evil: I couldn\'t find a voice channel! Please specify one or join one!')

    vc = ctx.voice_client

    if vc:
        if vc.channel.id == channel.id:
            return
        try:
            await vc.move_to(channel)
        except asyncio.TimeoutError:
            await ctx.send(f':see_no_evil: The voice channel timed out.')
    else:
        try:
            await channel.connect()
        except asyncio.TimeoutError:
            await ctx.send(f':see_no_evil: The voice channel timed out.')


@client.command()
async def gif_custom(ctx, rating: str, *, query: str):
    gif_url = get_gif(query, rating)
    await ctx.send(gif_url)


@client.command()
async def fact(ctx):
    embed = discord.Embed(
        title=":thinking: Monkey Fact:",
        description=random.choice(monkey_facts),
        colour=discord.Colour.dark_orange()
    )
    embed.set_footer(text='MonkeBot')
    queries = ["thinking monkey", "monkey thinking"]
    embed.set_image(url=get_image(queries, 10))
    await ctx.send(embed=embed)


@client.command()
async def shoot(ctx, *, member=None):
    # print(member)
    # print(type(member))
    if member is None:
        await ctx.send(f":see_no_evil: Who do I shoot?")
        await ctx.send("https://i.pinimg.com/originals/b3/67/0b/b3670b4268ead84ca68abf8869cd3053.gif")
        return

    if member == "me":
        await ctx.send(f"Much obliged.")
        await ctx.send("https://media1.giphy.com/media/l1HhpeYMyCiyz16Sy0/giphy.gif?cid=ecf05e478wa3ucziq7vwyjcqj9um0b383s83846r7j0kobxl&rid=giphy.gif")
        return

    members = [m for m in client.get_all_members() if not m.bot]

    if member == "someone":
        member = random.choice(members)
        await ctx.send(f"Monke shoots {member.display_name}!")
        await ctx.send(random.choice(shooting_gifs))
        return

    elif member == "monke" or member == "monkey" or member == MONKE_BOT_ID:
        await ctx.send(f"Monke is not amused.")
        await ctx.send("https://media.tenor.com/images/fd2624e374d9064d4721803c85f86f19/tenor.gif")

    member = member[3:-1]  # Gets the raw id of the user.
    for m in members:
        if str(m.id) == member:
            await ctx.send(f"Monke shoots {m.display_name}!")
            await ctx.send(random.choice(shooting_gifs))
            return

    await ctx.send(f":see_no_evil: I don't know who that is!")
    await ctx.send("https://i.pinimg.com/originals/b3/67/0b/b3670b4268ead84ca68abf8869cd3053.gif")
    return




@client.command()
async def gif(ctx, *, query: str):
    if query == "":
        gif_url = get_gif("monkey", "g")
    else:
        gif_url = get_gif(query, "g")
    await ctx.send(gif_url)


# noinspection PyBroadException
@client.command()
async def screech(ctx):
    try:
        channel = ctx.author.voice.channel
    except AttributeError:
        await ctx.send(f':see_no_evil: I couldn\'t find a voice channel! Please join one!')

    vc = ctx.voice_client

    if vc:
        print('vc')
        if not vc.channel.id == channel.id:
            print('not vc same channel')
            try:
                await vc.move_to(channel)
                vc = ctx.voice_client
            except asyncio.TimeoutError:
                await ctx.send(f':see_no_evil: The voice channel timed out.')

    else:
        print('no vc')
        try:
            print('connecting')
            await channel.connect()
            vc = ctx.voice_client

        except asyncio.TimeoutError:
            await ctx.send(f':see_no_evil: The voice channel timed out.')

    sound = random.choice(screech_sounds)

    vc.play(discord.FFmpegPCMAudio(sound))
    vc.source = discord.PCMVolumeTransformer(vc.source)
    vc.source.volume = 1
    await asyncio.sleep(11)
    await vc.disconnect()


@client.command(aliases=['Monke'])
async def monke(ctx):
    gif_url = get_gif("monkey", "g")
    await ctx.send(gif_url)


@client.command(aliases=['Angry', 'angre', 'Angre'])
async def angry(ctx):
    queries = ["angry monkey", "mad monkey"]
    link = get_image(queries, 10)
    await ctx.send(link)


@client.command(aliases=['8ball'])
async def _8ball(ctx, *, question):

    embed = discord.Embed(
        title=":8ball:8ball",
        description="Monke shakes the 8ball...",
        colour=discord.Colour.blurple()
    )

    if question[-1] != '?':
        question += '?'

    embed.set_footer(text='MonkeBot')
    embed.add_field(name=':8ball:Question', value=question, inline=False)

    embed.add_field(name=':8ball:Answer', value=random.choice(_8ball_responses), inline=False)
    await ctx.send(embed=embed)


@client.command(aliases=['Hi', 'hi', 'Hello'])
async def hello(ctx):

    embed = discord.Embed(
        title=":monkey: Monke says...",
        description="Hi, I'm Paul!",
        colour=discord.Colour.dark_orange()
    )
    embed.set_footer(text='MonkeBot')
    embed.set_image(url="https://thumbs.gfycat.com/AgitatedAgreeableAnkolewatusi-size_restricted.gif")

    await ctx.send(embed=embed)

"""
@client.event
async def on_command_error(ctx, error):
    await ctx.send(error)
"""

client.run(DISCORD_TOKEN)
