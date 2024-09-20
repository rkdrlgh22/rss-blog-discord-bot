import feedparser
import discord
import asyncio
from bs4 import BeautifulSoup
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer

# Discord 봇 설정
TOKEN = 'DISCORD BOT TOKEN'
CHANNEL_IDS = [channel id, channel id]  # 알림을 보낼 디스코드 채널 ID 목록

# RSS 피드 URL 목록
RSS_URLS = [
    'https://rss.blog.naver.com/rkdrlgh22.xml',
    'https://rkdrlgh22.tistory.com/rss'
]

# 마지막으로 확인한 피드 항목의 링크를 저장
last_entry_links = {url: None for url in RSS_URLS}

# Discord 클라이언트 설정
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

def summarize_text(text, sentence_count=3):
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer = LsaSummarizer()
    summary = summarizer(parser.document, sentence_count)
    return "\n".join(str(sentence) for sentence in summary)

def clean_html(html):
    soup = BeautifulSoup(html, "html.parser")
    return soup.get_text()

async def check_rss_feed():
    await client.wait_until_ready()
    channels = [client.get_channel(channel_id) for channel_id in CHANNEL_IDS]
    
    while not client.is_closed():
        for url in RSS_URLS:
            feed = feedparser.parse(url)
            if feed.entries:
                latest_entry = feed.entries[0]
                if latest_entry.link != last_entry_links[url]:
                    clean_summary = clean_html(latest_entry.summary)
                    summary = summarize_text(clean_summary)
                    message = f"새로운 게시글\n> ## 제목 : {latest_entry.title}\n> ### 내용 : \n```{summary}```\n> 링크: {latest_entry.link}"
                    for channel in channels:
                        await channel.send(message)
                    last_entry_links[url] = latest_entry.link
        await asyncio.sleep(3)  # 3초마다 피드 확인

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')
    client.loop.create_task(check_rss_feed())

client.run(TOKEN)
