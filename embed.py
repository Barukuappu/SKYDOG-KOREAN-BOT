import discord
from discord.ext import commands
from to import Token

bot = commands.Bot(command_prefix="!")


@bot.event
async def on_ready():
    print(f'embed 부팅 성공!')


@bot.command()
async def 봇(ctx):
    embed = discord.Embed(title="스독이는 금지어 필터링을 하는 봇이야.",
                          description="**!안녕**\n내가 인사를 해 줘.\n\n**!공지사항**\n최근 업데이트 내역이 나올거야.\n\n**!봇**\n지금 네가 입력한 명령어야.\n\n**!게임**\n나랑 할 수 있는 게임의 명령어가 나와. 자세한 건 **!게임**을 쳐봐.",
                          color=0xff8984)
    embed.set_footer(text="SKYDOG")
    await ctx.send(embed=embed)


@bot.command()
async def 게임(ctx):
    embed = discord.Embed(title="나랑 같이 게임하자!",
                          description="**!뽑기**\n내가 좋아하는 것들을 뽑을 수 있어.\n\n**!가위바위보 (가위 or 바위 or 보)**\n나랑 가위바위보를 할 수 있어.\n\n**!복권**\n실제 복권마냥 숫자를 뽑을 수 있어.\n\n**그 외에 것은?**\n나중에 추가될 수 있어.",
                          color=0xff8984)
    embed.set_footer(text="SKYDOG")
    await ctx.send(embed=embed)

@bot.command()
async def 공지사항(ctx):
    embed = discord.Embed(title="공지사항",
                          description="**20211206**\n내가 Github와 Heroku의 도움을 빌렸어. 이제 나랑 24시간 동안 놀 수 있을거야!\n\n**20211205**\n내 봇이 산골호랑국에 들어간 날이야. 마이너 업데이트로 게임 결과에 본인의 닉네임이 나오도록 했어.\n\n",
                          color=0xff8984)
    embed.set_footer(text="SKYDOG")
    await ctx.send(embed=embed)


bot.run(Token)
