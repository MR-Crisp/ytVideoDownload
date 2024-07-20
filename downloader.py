from yt_dlp import YoutubeDL

URLS = ['https://www.youtube.com/shorts/NsMKvVdEPkw']
with YoutubeDL() as ydl:
    ydl.download(URLS)