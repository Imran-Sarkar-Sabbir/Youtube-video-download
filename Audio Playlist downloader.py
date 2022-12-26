import threading
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


def download(url):
    print(f"Downloading.. {url}")
    audio = pytube.YouTube(url,
    on_progress_callback=on_progress,
    on_complete_callback=completed_function,
    ).streams.get_audio_only()
    audio_download = audio.download(output_path=f'{dirname}/download/audios_v1')
    base, ext = os.path.splitext(audio_download)
    new_file = base + '.mp3'
    os.rename(audio_download, new_file)




for url in url_list:
    download(url)

""" Uncomment for use multi-threading download """
# thead_list = []
# for url in url_list: 
#     t = threading.Thread(target=download, name=url, args=(url,))
#     t.start()
#     thead_list.append(t)

# for t in thead_list:
#     t.join()

print("All Files are downloaded.")