import random
from discord.ext import commands
from to import Token

bot = commands.Bot(command_prefix="!")


@bot.event
async def on_ready():
    print(f'게임 부팅 성공!')


@bot.command()
async def 뽑기(ctx):
    minerals = ['덤벨 5kg', '덤벨 10kg', '푸시업바', '덤벨 50kg', '프로틴']
    weights = [5, 10, 11, 50, 80]
    results = random.choices(minerals, weights=weights, k=1)
    await ctx.send(', '.join(results) + '이/가 나왔어.' + ' ' + ctx.message.author.name + '!')


@bot.command()
async def 가위바위보(ctx, user: str):
    rps_table = ['가위', '바위', '보']
    bot = random.choice(rps_table)
    result = rps_table.index(user) - rps_table.index(bot)
    if result == 0:
        await ctx.send(f'**{user} vs {bot}** 비겼어.' + ' ' + ctx.message.author.name + '.')
    elif result == 1 or result == -2:
        await ctx.send(f'**{user} vs {bot}** 네가 이겼어.' + ' ' + ctx.message.author.name + '!')
    else:
        await ctx.send(f'**{user} vs {bot}** 내가 이겼네?' + ' ' + ctx.message.author.name + '?')


bot.run(Token)
