from pytube import YouTube

def ytd1(link):
    # link=input("enter youtube video link:  ")
    #link =  "https://www.youtube.com/watch?v=ypX1hBbT0xU"
    yt = YouTube(link)
    yt.streams.first().download()


def download_360p_mp4_videos(url: str, outpath: str = "./"):

    yt = YouTube(url)

    yt.streams.filter(file_extension="mp4").get_by_resolution("360p").download(outpath)
    print("Downloading")

if __name__ == "__main__":
    #link = "https://www.youtube.com/watch?v=ypX1hBbT0xU"
    link=input("enter youtube video link:  ")
    spath=""
    #spath=input("enter path to save file")
    download_360p_mp4_videos(link,spath)