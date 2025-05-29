from pytube import YouTube

def download_video():
    try:
        url=input("Enter youtube url: ")
        yt=YouTube(url)

        print(f"Title {yt.title}")
        print("Downloading")

    #get high resolution

        video=yt.streams.get_highest_resolution()
        video.download()

    except Exception as e:
        print("Error Occured ",e)

download_video()


