from pytube import YouTube
from pytube.exceptions import VideoUnavailable
from sys import argv



link = argv[1]
yt = YouTube(link)
print(f"Title: {yt.title}.")
print(f"Views: {yt.views}")
print(f"Video length: {round(yt.length / 60, 2)} minutes.")
try:
    stream = yt.streams.get_highest_resolution()
    stream.download()
except VideoUnavailable:
    print(f"Video {link} is unavailable, skipping")
else:
    print(f"Downloading video: {yt.title}.")
