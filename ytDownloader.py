from pytube import YouTube
import os
import datetime

# Function that tracks the download progress
def download_progress (stream, _, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    completion_percentage = int(bytes_downloaded / total_size * 100)
    print(f"↴ Downloading ... {completion_percentage} %")

# Define variables
link = input("Please insert the YouTube URL: ")
user_choice = input("Do you want to download only audio, only video or both [a/v/b]: ")

# Create output directories if they don't exist
audio_download_location = 'D:\Multimedia\YouTube Downloads\Audio'
video_download_location = 'D:\Multimedia\YouTube Downloads\Video'
os.makedirs(audio_download_location, exist_ok=True)
os.makedirs(video_download_location, exist_ok=True)

try:
    # Printing information in the terminal
    yt = YouTube(link)
    print("\n☛ Title: ", yt.title)
    print("☛ Views: ", yt.views)
    print("☛ Duration: ", str(datetime.timedelta(seconds=yt.length)))

    #Register the callback progress
    yt.register_on_progress_callback(download_progress) 

    # Download the audio and/or video files
    if user_choice in ["a", "b"]:
        ys = yt.streams.get_audio_only()
        downloaded_audio = ys.download(audio_download_location)
   
    if user_choice in ["v", "b"]:
        #yv = yt.streams.filter(only_video=True, mime_type="video/mp4").asc().first()
        yv = yt.streams.filter(only_video=True).asc().first()
        downloaded_video = yv.download(video_download_location)

    # Rename the file from .mp4 to .mp3
    if user_choice != "v":
        split_audio = os.path.splitext(downloaded_audio)
        os.rename(downloaded_audio, split_audio[0] + ".mp3")
    # Rename the video from .webm to .mp4
    elif user_choice != "a":
        split_video = os.path.splitext(downloaded_video)
        os.rename(downloaded_video, split_video[0] + ".mp4")

    print(f"\n✔ Download finished!\n")

except Exception as e:
    print("\n❌ Error occurred while downloading: ", str(e))