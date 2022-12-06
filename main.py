import argparse
from pytube import YouTube

VIDEO_SAVE_DIRECTORY = "./videos"
AUDIO_SAVE_DIRECTORY = "./audio"

def download(video_url):
    video = YouTube(video_url)
    video = video.streams.get_highest_resolution()

    try:
        video.download(VIDEO_SAVE_DIRECTORY)
    except:
        print("Failed to download video")

    print("video was downloaded successfully")

def download_audio(video_url):
    video = YouTube(video_url)
    audio = video.streams.filter(only_audio = True).first()

    try:
        audio.download(AUDIO_SAVE_DIRECTORY)
    except:
        print("Failed to download audio")

    print("audio was downloaded successfully")

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("-v", "--video", required = True, help = "URL to youtube video")
    ap.add_argument("-a", "--audio", required = False, help = "audio only", action = argparse.BooleanOptionalAction)
    args = vars(ap.parse_args())

    if args["audio"]:
        download_audio(args["video"])
    else:
        download(args["video"])
