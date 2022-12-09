import requests
from bs4 import BeautifulSoup
import discord
from discord.ext import tasks

intents = discord.Intents.default()
intents.message_content = True
url = 'https://fun.ssu.ac.kr/ko/program/all/view/%d' #URL 형식
n = 3072 #URL 게시글 번호 

def print_all():
    
    global title, human, grade, depart, act_date, date, people, email, phone_number, place, info
    # 제목
    title = soup.find("h4")
    print(title.string)

    # 모집대상, 학년/성별, 학과
    info_list1=[]
    sl=soup.select('ul>li>span')
    for list in sl[0:3]:
        info_list1.append(list.get_text())
    
    human=info_list1[0]
    grade=info_list1[1].strip()
    depart=info_list1[2].strip()

    # 활동기간, 신청기간, 신청인원
    info_list2=[]
    sl=soup.select('div>form>ul>li>span') 
    for list in sl[6:]:
        info_list2.append(list.get_text())
    list2_len=len(info_list2)

    for i in range(list2_len):
        if i%3==0:
            act_date=info_list2[i].replace("\n","")
        elif i%3==1:
            date=info_list2[i].strip()
            date=date.replace("\n"," ")
        elif i%3==2:
            people=info_list2[i].replace("\n","")
            people=people.replace("\t","")

    # 이메일주소, 연락처, 장소
    info_list3=[]
    sl=soup.select('ul>li>div>span')
    for list in sl[1:4]:
        info_list3.append(list.get_text())
    for i in range(3):
        if i%3==0:
            email = info_list3[i]
        elif i%3==1:
            phone_number = info_list3[i]
        elif i%3==2:
            place = info_list3[i]

    # 카테고리
    l_list=[]
    sl=soup.select('ul>li>div.category')
    for list in sl[1:2]:
        l_list.append(list.get_text())
    info=l_list[0].replace("\t","")
    info=info.replace("\n","")
    info=info.split()[0]
    

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    test.start()

@tasks.loop(minutes=10)
 # n초마다 다음 메시지 출력
async def test():
    global n, soup
    request= requests.get(url %n) #URL 게시글 번호에 따른 인터넷 주소 정보 받아오기
    soup = BeautifulSoup(request.text, "lxml") #lxml 형식으로 내용을 받아옴
    if (request.ok):
        print_all()
        n+=1
        channel = client.get_channel(1050414319671717888)
        all = title.string + "\n" + "모집대상: "+ human + "\n" + "학년/성별: "+ grade + "\n" + "학과: "+ depart + "\n" + "활동기간: " + act_date + "\n" + "신청기한: " + date + "\n" + "신청인원: " + people + "\n" +  "이메일: " + email + "\n" + "연락처: " + phone_number + "\n" + "장소: " + place + "\n" + "카테고리: " + info + "\n" + "주소: " + url %n + "\n" #채널 센드는 하나의 인수만 받을 수 있기 때문에 +로 모두 인수들을 묶어서 all 변수로 출력함
        await channel.send(all)
    else:
        print("정보를 기다리는 중")

client.run('MTAyNzA3NzcwNjk3MTYyNzU4MA.Gkmgap.6nLvtT5ijzGmx0VUC6a7zcbZb4n3XOSXeOimXg')