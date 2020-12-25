import discord
import requests
import json
import asyncio
import logging
from datetime import datetime
import time
import requests
import json

client = discord.Client()

logger = logging.getLogger('discord')
logger.setLevel(logging.WARNING)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='a')
handler.setFormatter(logging.Formatter('[%(levelname)s] %(asctime)s - %(name)s: %(message)s'))
logger.addHandler(handler)
#로그 작성
now = time.localtime()


@client.event
async def on_ready():

    print(f'{client.user}으로 로그인 성공')
    logger.info(f'{client.user}으로 로그인 성공')

    activity = discord.Activity(name="ㅎ ㅏ..학교 가기 싫다", type=discord.ActivityType.playing)
    await client.change_presence(activity=activity)
#기본적인 로그인 확인, 상태메시지 설정

@client.event
async def on_message(message):
    content = message.content

    if message.author == client.user:
        return
    #봇의 말에 대답하는것 방지
    if content == "k/오늘급식":
        data = datetime.today().strftime("%Y%m%d")
        url = f'https://open.neis.go.kr/hub/mealServiceDietInfo?key=(open.neis.go.kr 에서 받은 인증키)&Type=JSON&ATPT_OFCDC_SC_CODE=(교육청코드)&SD_SCHUL_CODE=(학교코드)&MLSV_YMD={data}'
        response = requests.get(url)
        response_json = json.loads(response.text)
        try:
            resulta = response_json['mealServiceDietInfo'][1]['row'][0]['DDISH_NM']
            resulta = resulta.replace("<br/>", "\n")
            resulta = resulta.replace("*", "")
            print(resulta)
            await message.channel.send(f"오늘의 급식 \n {resulta}")
        except KeyError:
            await message.channel.send("오늘의 급식 정보가 아직 없어요 ㅠ")
            
    if content.startswith("k/급식"):
        data = content.replace("k/급식 ","")
        url = f'https://open.neis.go.kr/hub/mealServiceDietInfo?key=(open.neis.go.kr에서 받은 인증키)&Type=JSON&ATPT_OFCDC_SC_CODE=(교육청코드)&SD_SCHUL_CODE=(학교코드)&MLSV_YMD={data}'
        response = requests.get(url)
        response_json = json.loads(response.text)
        try:
            resulta = response_json['mealServiceDietInfo'][1]['row'][0]['DDISH_NM']
            resulta = resulta.replace("<br/>", "\n")
            resulta = resulta.replace("*", "")
            resulta = resulta.replace("^", "")
            print(resulta)
            await message.channel.send(f"그날의 급식 \n {resulta}")
        except KeyError:
            await message.channel.send("그날의 급식 정보가 없어요 ㅠ")
    if content.startswith("k/시간표"):
        grade = content[6:7]
        date = content[10:18]
        classNM = content[8:9]
        url =f'https://open.neis.go.kr/hub/elsTimetable?key=(open.neis.go.kr에서 받은 인증키)&Type=json&pIndex=1&pSize=100&ATPT_OFCDC_SC_CODE=(교육청코드)&SD_SCHUL_CODE=(학교코드)&GRADE={grade}&CLASS_NM={classNM}&ALL_TI_YMD={date}'
        response = requests.get(url)
        response_json = json.loads(response.text)
        print(response_json)
        classtime = [0,1,2,3,4,5,6]
        for a in classtime:
            try:
                resulta = response_json['elsTimetable'][1]['row'][a]['ITRT_CNTNT']
                await message.channel.send(resulta)
            except IndexError:
                break


client.run("디스코드 봇 토큰")
