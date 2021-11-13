import discord, asyncio
import os

client = discord.Client()

@client.event
async def on_ready():
    print('{0.user} 봇을 연결했습니다'.format(client))

@client.event
async def on_message(message):
    if message.content.startswith("~투표"):
        vote = message.content[4:].split("/")
        await message.channel.send("투표 - " + vote[0])
        for i in range(1, len(vote)):
                choose = await message.channel.send("```" + vote[i] + "```")
                await choose.add_reaction('👍')
                
@client.event
async def on_message(message):
    if message.content.startswith ("!청소"):
        if message.author.guild_permissions.administrator:
            amount = message.content[4:]
            await message.delete()
            await message.channel.purge(limit=int(amount))

            embed = discord.Embed(title="메시지 삭제 알림", description="디스코드 채팅 {}개가\n{}님의 요청으로 인해 삭제 되었습니다".format(amount, message.author), color=0x000000)
            embed.set_footer(text="Bot Made by. 킹갓제네럴엠페러프레시뷰티풀하이클래스E클래스하이마트ddoiy #7903")
            await message.channel.send(embed=embed)
        
        else:
            await message.delete()
            await message.channel.send("{}, 당신은 명령어를 사용할 수 있는 권한이 없습니다".format(message.author.mention))
            
            
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('~도움말'):
        await message.channel.send('~청소[숫자]-넣은 숫자만큼 챗을 없앰.   ~투표/[제목]/[투표항목1]/[투표항목2]-투표기능   ~공지-공지기능(도라지 스튜디오 서버에서만 사용 가능.)')

access_token = os.environ['BOT_TOKEN']
client.run(access_token)

