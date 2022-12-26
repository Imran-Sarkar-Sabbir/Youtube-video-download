import pytube
import os


dirname = os.path.dirname(__file__)
yt_url = input("Link Here :")


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


# yt = pytube.YouTube(link,
#                     on_progress_callback=on_progress,
#                     on_complete_callback=completed_function,
#                     use_oauth=False,
#                     allow_oauth_cache=True)

# yt.streams\
#     .get_audio_only()\
#     .filter(progressive=True, file_extension='mp3')\
#     .order_by('resolution')\
#     .desc()\
#     .first()\
#     .download(f'{dirname}/download/audios')

def download(yt_url):
    audio = pytube.YouTube(yt_url,
    on_progress_callback=on_progress,
    on_complete_callback=completed_function,
    ).streams.get_audio_only()

    audio_download = audio.download(output_path=f'{dirname}/download/audios')
    base, ext = os.path.splitext(audio_download)
    new_file = base + '.mp3'
    os.rename(audio_download, new_file)

download(yt_url)