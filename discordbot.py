import discord, requests, urllib
from bs4 import BeautifulSoup
import asyncio

client = discord.Client()

@client.event
async def on_ready():
    print("봇이 성공적으로 실행되었습니다.")
    await client.change_presence(activity=discord.Game(f"WaplarL.com"), status=discord.Status.online)
    await asyncio.sleep(5)
    await client.change_presence(activity=discord.Game(f"빠른지원"), status=discord.Status.online)
    await asyncio.sleep(5)


@client.event
async def on_message(message):
    async def makeembed3(title):
        embed=discord.Embed(
            title=title,
            colour=discord.Colour.red()
        )
        await message.channel.send(embed=embed)

    async def makeembed4(title, description):
        embed=discord.Embed(
            title=title,
            description=description,
            colour=discord.Colour.red()
        )
        await message.channel.send(embed=embed)
    if message.guild is None:
        if message.author.bot:
            return
        else:
            await message.add_reaction("✅")
            embed = discord.Embed(colour=discord.Colour.blue(), timestamp=message.created_at)
            embed.add_field(name='전송자', value=message.author, inline=False)
            embed.add_field(name='내용', value=message.content, inline=False)
            embed.set_footer(text=f'.답변 <@{message.author.id}> [할말] 을 통해 답변을 보내주세요.')
            await client.get_channel(1099643082179354704).send(f"`{message.author.name}({message.author.id})`", embed=embed)

    if message.content.startswith('.답변'):
        if message.author.id == 533683323390918666 or message.author.id == 727046350822309909:
            user_id = message.mentions[0].id
            user_name = message.mentions[0]
            amount = message.content[26:]
            userss = await client.fetch_user(user_id)
            await userss.send(f"**```yaml\n안녕하세요. {user_name} 고객님,\nWaplarL.com 고객센터입니다.\n문의주신 질문에 대한 답변입니다.\n\n{amount}\n\n오늘도 저희 WaplarL.com를 이용해주셔서 감사합니다.\n오늘 하루도 건승하세요.```**")
            await message.channel.send(f'`{message.mentions[0]}`**에게 디엠을 전송했습니다 :white_check_mark:**')
        else:
            return
    
    if message.content.startswith('.쪽지'):
        if message.author.id == 533683323390918666 or message.author.id == 727046350822309909:
            user_id = message.mentions[0].id
            user_name = message.mentions[0]
            amount = message.content[26:]
            userss = await client.fetch_user(user_id)
            await userss.send(f"**```yaml\n안녕하세요. {user_name} 고객님,\nWaplarL.com 관리진에서 보낸 쪽지입니다.\n\n{amount}\n\n오늘도 저희 WaplarL.com를 이용해주셔서 감사합니다.\n오늘 하루도 건승하세요.```**")
            await message.channel.send(f'`{message.mentions[0]}`**에게 디엠을 전송했습니다 :white_check_mark:**')
        else:
            return
        
        
client.run(token)
