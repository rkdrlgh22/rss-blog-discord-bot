# Discord RSS Feed Notifier Bot

이 프로젝트는 특정 RSS 피드를 모니터링하고 새로운 게시글이 올라올 때마다 디스코드 채널에 알림을 보내는 디스코드 봇입니다.

## 기능

- 지정된 RSS 피드를 3초마다 확인합니다.
- 새로운 게시글이 있을 경우 디스코드 채널에 알림을 보냅니다.
- 알림 메시지는 게시글의 제목, 요약된 내용, 링크를 포함합니다.

## 설치

1. Python 3.x를 설치합니다.
2. 필요한 라이브러리를 설치합니다:

```sh
python3 -m pip install feedparser discord.py beautifulsoup4 sumy nltk
```

3. `nltk` 라이브러리의 `punkt` 데이터를 다운로드합니다:

```python
import nltk
nltk.download('punkt')
```

## 사용 방법

1. `playbot3.py` 파일을 생성하고 다음 코드를 복사하여 붙여넣습니다:

2. `YOUR_DISCORD_BOT_TOKEN`을 실제 디스코드 봇 토큰으로, `YOUR_CHANNEL_ID_1`과 `YOUR_CHANNEL_ID_2`를 실제 디스코드 채널 ID로 변경합니다.

3. 스크립트를 실행합니다:
