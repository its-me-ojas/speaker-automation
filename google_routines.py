import sys
from gtts import gTTS
from playsound import playsound


def text_to_speech(text, lang='en'):
    tts = gTTS(text=text, lang=lang, slow=False)
    tts.save("output.mp3")  # Save the generated speech to an MP3 file
    play_mp3("output.mp3")  # Play the saved MP3 file


def play_mp3(file_path):
    try:
        playsound(file_path)
    except KeyboardInterrupt:
        sys.exit("Music playback stopped.")


# Replace 'Hello, how are you?' with the text you want to convert to speech
text_to_speech("Hushraj, are you gay, do you like dicks?? wanna suck on them?")
