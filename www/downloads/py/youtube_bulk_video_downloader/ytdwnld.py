import youtube_dl

def download_v(link):
    try:
        ydls = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }]
        }
        with youtube_dl.YoutubeDL(ydls) as yt:
            yt.download(link)
    except youtube_dl.utils.DownloadError as e:
        print("Invalid link")

links = input('Enter links with spaces!')
lList = links.split(' ')

download_v(lList)
