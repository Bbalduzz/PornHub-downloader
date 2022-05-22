#!/usr/bin/env python
import youtube_dl
from rich import print
from rich.console import Console
from bs4 import BeautifulSoup
import requests

r = Console()

print('''
 _______                              [yellow]    __    __          __       [/yellow] 
|       \                             [yellow]   |  \  |  \        |  \      [/yellow]
| ▓▓▓▓▓▓▓\ ______   ______  _______   [yellow]   | ▓▓  | ▓▓__    __| ▓▓____  [/yellow]
| ▓▓__/ ▓▓/      \ /      \|       \  [yellow]   | ▓▓__| ▓▓  \  |  \ ▓▓    \ [/yellow]
| ▓▓    ▓▓  ▓▓▓▓▓▓\  ▓▓▓▓▓▓\ ▓▓▓▓▓▓▓\ [yellow]   | ▓▓    ▓▓ ▓▓  | ▓▓ ▓▓▓▓▓▓▓ [/yellow]
| ▓▓▓▓▓▓▓| ▓▓  | ▓▓ ▓▓   \▓▓ ▓▓  | ▓▓ [yellow]   | ▓▓▓▓▓▓▓▓ ▓▓  | ▓▓ ▓▓  | ▓▓ [/yellow]
| ▓▓     | ▓▓__/ ▓▓ ▓▓     | ▓▓  | ▓▓ [yellow]   | ▓▓  | ▓▓ ▓▓__/ ▓▓ ▓▓__/ ▓▓ [/yellow]
| ▓▓      \▓▓    ▓▓ ▓▓     | ▓▓  | ▓▓ [yellow]   | ▓▓  | ▓▓\▓▓    ▓▓ ▓▓    ▓▓ [/yellow]
 \▓▓       \▓▓▓▓▓▓ \▓▓      \▓▓   \▓▓ [yellow]    \▓▓   \▓▓ \▓▓▓▓▓▓ \▓▓▓▓▓▓▓ [/yellow]

  _______    ______   __       __  __    __  __        ______    ______   _______   ________  _______  
|       \  /      \ |  \  _  |  \|  \  |  \|  \      /      \  /      \ |       \ |        \|       \ 
| ▓▓▓▓▓▓▓\|  ▓▓▓▓▓▓\| ▓▓ / \ | ▓▓| ▓▓\ | ▓▓| ▓▓     |  ▓▓▓▓▓▓\|  ▓▓▓▓▓▓\| ▓▓▓▓▓▓▓\| ▓▓▓▓▓▓▓▓| ▓▓▓▓▓▓▓
| ▓▓  | ▓▓| ▓▓  | ▓▓| ▓▓/  ▓\| ▓▓| ▓▓▓\| ▓▓| ▓▓     | ▓▓  | ▓▓| ▓▓__| ▓▓| ▓▓  | ▓▓| ▓▓__    | ▓▓__| ▓▓
| ▓▓  | ▓▓| ▓▓  | ▓▓| ▓▓  ▓▓▓\ ▓▓| ▓▓▓▓\ ▓▓| ▓▓     | ▓▓  | ▓▓| ▓▓    ▓▓| ▓▓  | ▓▓| ▓▓  \   | ▓▓    ▓▓
| ▓▓  | ▓▓| ▓▓  | ▓▓| ▓▓ ▓▓\▓▓\▓▓| ▓▓\▓▓ ▓▓| ▓▓     | ▓▓  | ▓▓| ▓▓▓▓▓▓▓▓| ▓▓  | ▓▓| ▓▓▓▓▓   | ▓▓▓▓▓▓▓
| ▓▓__/ ▓▓| ▓▓__/ ▓▓| ▓▓▓▓  \▓▓▓▓| ▓▓ \▓▓▓▓| ▓▓_____| ▓▓__/ ▓▓| ▓▓  | ▓▓| ▓▓__/ ▓▓| ▓▓_____ | ▓▓  | ▓▓
| ▓▓    ▓▓ \▓▓    ▓▓| ▓▓▓    \▓▓▓| ▓▓  \▓▓▓| ▓▓      \▓▓    ▓▓| ▓▓  | ▓▓| ▓▓    ▓▓| ▓▓     \| ▓▓  | ▓▓
 \▓▓▓▓▓▓▓   \▓▓▓▓▓▓  \▓▓      \▓▓ \▓▓   \▓▓ \▓▓▓▓▓▓▓▓ \▓▓▓▓▓▓  \▓▓   \▓▓ \▓▓▓▓▓▓▓  \▓▓▓▓▓▓▓▓ \▓▓   \▓▓
                                                                                                      
                                                                                                      
                                                                                                                                                                                                               
                                                                    
''')

url = r.input("🔴 Porn-[yellow]Hub[/yellow] Video/Playlist Url:\n ")

directory = 'C:/Downloads/phmedias' # <== edit this to your preference

print(f"📂 Folder Directory: {directory}")

def video():
    go = True
    while go:
        if url == '':
            go = False
        else:
            dir = directory+'/videos/%(title)s.%(ext)s'
            page = requests.get(url)
            soup = BeautifulSoup(page.content, 'html.parser')
            vid_title = soup.find('span',{'class':'inlineFree'}).contents[0]
            ydl_opts = {
                'format': 'best',
                'outtmpl': dir,
                'nooverwrites': True,
                'no_warnings': False,
                'ignoreerrors': True,
            }

            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])

            print(f'🧲[green] {vid_title} has been downloaded[/green]')
        
def playlist():
    vids = []
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    name = soup.find('h1', {'class': 'playlistTitle'}).contents[0]
    print(f'🔭 Playlist [magenta]{name}[/magenta] is downloading...')
    videos = soup.find_all('a', {'href': True})
    for video in videos:
        vid = video['href']
        code = url.split("/")[-1]
        if 'view_video.php?' in vid and vid.endswith(code):
            vidUrl = f'https://www.pornhub.com{vid}'
            vids.append(vidUrl)
    for v in vids:
        if vids.count(v)>1:
            vids.remove(v)
        page = requests.get(v)
        soup = BeautifulSoup(page.content, 'html.parser')
        vid_title = soup.find('span',{'class':'inlineFree'}).contents[0]
        dir = directory+f'/playlists/{name}/%(title)s.%(ext)s'
        ydl_opts = {
            'format': 'best',
            'outtmpl': dir,
            'nooverwrites': True,
            'no_warnings': False,
            'ignoreerrors': True,
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([v])
        
        print(f'🧲[green] {vid_title} has been downloaded[/green]')

if 'playlist' in url:
    playlist()
else:
    video()
