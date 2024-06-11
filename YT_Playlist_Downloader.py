from pytube import Playlist

def download_youtube_playlist(playlist_url, download_path='.'):
    playlist = Playlist(playlist_url)
    print(f'Downloading playlist: {playlist.title}')
    
    for video in playlist.videos:
        print(f'Downloading video: {video.title}')
        video.streams.get_highest_resolution().download(output_path=download_path)
    print('Download completed.')

if __name__ == '__main__':
    playlist_url = input('Enter the URL of the YouTube playlist: ')
    download_path = input('Enter the path where you want to save the videos (default is current directory): ') or '.'
    
    download_youtube_playlist(playlist_url, download_path)
