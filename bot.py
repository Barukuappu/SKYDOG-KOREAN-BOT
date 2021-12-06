import discord
import traceback
from discord.ext import commands

import subprocess

from to import Token

bot = commands.Bot(command_prefix="!")


@bot.event
async def on_ready():
    print(f'{bot.user.name} 부팅 성공!')
    game = discord.Game("근육! 프로틴! 벌크업!")
    await bot.change_presence(status=discord.Status.dnd, activity=game)


@bot.command()
async def 안녕(ctx):
    await ctx.send("안녕, 나는 스독이야!")


@bot.event
async def on_command_error(ctx, error):
    tb = traceback.format_exception(type(error), error, error.__traceback__)
    err = [line.rstrip() for line in tb]
    errstr = '\n'.join(err)
    if isinstance(error, commands.NotOwner):
        await ctx.send('**이거.. 실제 스카이독만 쓸 수 있는 명령어야.**')
    else:
        print(errstr)


@bot.command()
@commands.is_owner()
async def 방해금지(ctx):
    game = discord.Game("근육! 프로틴! 벌크업!")
    await bot.change_presence(status=discord.Status.dnd, activity=game)
    await ctx.send('봇 상태를 방해금지로 바꿨어.')


@bot.command()
@commands.is_owner()
async def 온라인(ctx):
    game = discord.Game("근육! 프로틴! 벌크업!")
    await bot.change_presence(status=discord.Status.online, activity=game)
    await ctx.send('봇 상태를 온라인으로 바꿨어.')

subprocess.Popen('python embed.py')
subprocess.Popen('python filtering.py')
subprocess.Popen('python game.py')
subprocess.Popen('python lottery.py')

bot.run(Token)
