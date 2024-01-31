import time
import schedule
import requests
import pyttsx3
from gtts import gTTS
import os


def make_api_call():
    url = 'https://newsapi.org/v2/top-headlines?country=us&apiKey=e801a04f1ecf453b8d57f58ca4d14230'
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        # Extracting relevant information from the API response
        articles = data.get('articles', [])
        news_text = ""
        print("Creating a text summary of the news")
        for idx, article in enumerate(articles):
            source = article.get('source', {}).get('name', 'Unknown Source')
            title = article.get('title', 'No Title Available')
            description = article.get('description', 'No Description Available')
            url = article.get('url', 'No URL Available')

            news_text += f"{idx + 1}. {title}. {description}. Read more at {source}.\n"
        print("File summary created!!")
        speak_news(news_text)
        # Printing relevant parts
        print(f'Source: {source}\nTitle: {title}\nDescription: {description}\nURL: {url}\n{"-" * 50}')

    except requests.exceptions.RequestException as e:
        print("Error fetching API Request:", e)


def speak_news(news_text):
    temp_audio_file = "temp_news.mp3"

    try:
        tts = gTTS(news_text, lang='en')
        tts.save(temp_audio_file)
        print("mp3 file saved")

        # os.system("mpv", temp_audio_file)
    except Exception as e:
        print("Error generating tts file :", e)
    finally:
        os.remove(temp_audio_file)


# python tts
# def speak_news(news_text):
#     engine = pyttsx3.init()
#     engine.say(news_text)
#     engine.runAndWait()


# schedule.every().day.at("23:40").do(make_api_call)
# while True:
#     schedule.run_pending()
#     time.sleep(1)

make_api_call()
