from playsound import playsound
import signal
import sys


def play_mp3(file_path):
    try:
        playsound(file_path)
    except KeyboardInterrupt:
        # Handle keyboard interrupt (Ctrl+C) to stop the music
        sys.exit("Music playback stopped.")


# Replace 'your_mp3_file.mp3' with the actual file path
mp3_file_path = "./music/Narvent - Fainted.mp3"
play_mp3(mp3_file_path)
