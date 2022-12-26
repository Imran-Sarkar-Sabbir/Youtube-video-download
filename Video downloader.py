import pytube
import os


dirname = os.path.dirname(__file__)
yt_url = input("Link Here :")


playlist = pytube.Playlist(yt_url)


url_list = []

for url in playlist.video_urls:
    url_list.append(url)


def on_progress(stream, chunk, bytes_remaining):
    """Callback function"""
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    pct_completed = bytes_downloaded / total_size * 100
    print(f"Status: {round(pct_completed, 2)} %\r")


def completed_function(stream, file_path):
    """Callback function"""
    print("download conmpleted                                                        \r")
    print(f"downloaded : {file_path}.                                                 \r")



def startDownload(url):
    yt = pytube.YouTube(url,
                        on_progress_callback=on_progress,
                        on_complete_callback=completed_function,
                        use_oauth=False,
                        allow_oauth_cache=True)

    yt.streams\
        .filter(progressive=True, file_extension='mp4')\
        .order_by('resolution')\
        .desc()\
        .first()\
        .download(f'{dirname}/download/videos')


for url in url_list:
    startDownload(url)