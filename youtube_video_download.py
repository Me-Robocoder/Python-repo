import traceback
from pytube import YouTube

def download_youtube_video(video_url, download_path):
    yt = YouTube(video_url)
    try:
        # for maximum video resolution
        video_stream = yt.streams.get_highest_resolution()
        video_stream.download(download_path)
        print("Download successfull!!! with resolution: ", video_stream.resolution)
    except:
        print("error occurred!!!")
        traceback.print_exc()

if __name__ == "__main__":
    download_youtube_video(input("Enter video url: ")
                           or 'https://www.youtube.com/shorts/tJAFHQaL6w0',
                           input("Enter download path: ")
                           or './krishna-tribute-music')
