import yt_dlp


def download_youtube_video():
    url = input("Enter YouTube video URL: ").strip()

    ydl_opts = {
        'format': 'best',  # download best quality video+audio
        'outtmpl': '%(title)s.%(ext)s',  # save file as video title
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
            print("Download completed successfully!")
    except Exception as e:
        print("Error occurred:", e)


download_youtube_video()
