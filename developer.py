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
async def on_ready(): 
  async def message(games):
    await client.wait_until_ready()

    while not client.is_closed():
        for g in games:
            await client.change_presence(status = discord.Status.online, activity = discord.Game(~도움말을 입력해보세요!))
            await asyncio.sleep(10)
            
            
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('~도움말'):
        await message.channel.send('~청소[숫자]-넣은 숫자만큼 챗을 없앰.   ~투표/[제목]/[투표항목1]/[투표항목2]-투표기능   ~공지-공지기능(도라지 스튜디오 서버에서만 사용 가능.)')

access_token = os.environ['BOT_TOKEN']
client.run(access_token)

