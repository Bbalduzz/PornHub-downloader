#!/usr/bin/env python
import youtube_dl
from rich import print
from rich.console import Console
from bs4 import BeautifulSoup
import requests
import urllib.request
from urllib.error import HTTPError
import os
from PIL import Image

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

url = r.input("🔴 Porn-[yellow]Hub[/yellow] Url:\n ")

directory = 'C:/Downloads/phmedias' # <== edit this to your preference

print(f"📂 Folder Directory: {directory}")

def video():
    go = True
    while go:
        go = input('continue? (y/N): ')
        if go == 'y':
            url = r.input("🔴 Porn-[yellow]Hub[/yellow] Video/Playlist Url:\n ")
            page = requests.get(url)
            soup = BeautifulSoup(page.content, 'html.parser')
            vid_title = soup.find('span',{'class':'inlineFree'}).contents[0]
            print(f'Video Found:[yellow] {vid_title} [/yellow]')
            dir = directory+'/videos/%(title)s.%(ext)s'
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
        else:
            go = False
        
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
        
def pornstar():
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    finder = soup.find(class_='nameSubscribe')
    name = finder.find(itemprop='name').text.replace('\n', '').strip()
    r.print(f"🔭 [magenta]{name}[/magenta]'s profile is being scraped. Kinda long process. Have a coffe mate")
    urls = []
    for i in range(1,10):
        Url = f'{url}/videos/upload?page={i}'
        urls.append(Url)
    valid_urls = []
    for u in urls:
        try:
            urllib.request.urlopen(u).getcode()
            valid_urls.append(u)
        except HTTPError:
            urls.remove(u)
    ## begin webscraping
    for vu in valid_urls:
        vids = []
        page = requests.get(vu)
        soup = BeautifulSoup(page.content, 'html.parser')
        videos = soup.find_all('a', {'href': True})
        for video in videos:
            vid = video['href']
            if 'view_video.php?' in vid:
                vidUrl = f'https://www.pornhub.com{vid}'
                vids.append(vidUrl)
        for vi in vids:
            if vids.count(vi)>1:
                vids.remove(vi)
            new_list = vids[next((i+2 for i, vi in enumerate(vids) if '&pkey=' in vi), len(vids)):]
        for v in new_list:
            page = requests.get(v)
            soup = BeautifulSoup(page.content, 'html.parser')
            vid_title = soup.find('span',{'class':'inlineFree'}).contents[0]
            dir = directory+f'/pornstars/{name}/%(title)s.%(ext)s'
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
            
def photos():
    for n in range(1,2):
        urls = f'{url}?page={n}'
    for url in urls:
        page = requests.get(url)
        soup = BeautifulSoup(page.content,'html.parser')
        finder = soup.find(class_='nameSubscribe')
        name = finder.find(itemprop='name').text.replace('\n', '').strip()
        print(f'🔭 Scraping [magenta]{name}[/magenta] albums...')
        albums = soup.find_all('a',{'href':True})
        # get the valid albums links
        album_links = []
        for album in albums:
            album_link_suffix = album['href']
            if 'album' in album_link_suffix:
                album_url = f'https://www.pornhub.com{album_link_suffix}'
                album_links.append(album_url)
            new_list = album_links[next((i+1 for i, album in enumerate(album_links) if 'albums?search=boobs' in album), len(album_links)):]
        # get the valid images links
        img_links = []
        for al in new_list:
            page = requests.get(al)
            soup = BeautifulSoup(page.content,'html.parser')
            title = soup.find(class_='photoAlbumTitleV2').contents[0].strip()
            if title == None:
                pass
            print(f"    ➡️ Scanning {name} [magenta]{title}[/magenta] album...")
            images = soup.find_all('a',{'href':True})
            for img in images:
                img_link_suffix = img['href']
                if 'photo/' in img_link_suffix:
                    img_url = f'https://www.pornhub.com{img_link_suffix}'
                    img_links.append(img_url)
        # downlaod images
        for image_link in img_links:
            checker = image_link.rsplit('/', 1)[1]
            page = requests.get(image_link)
            soup = BeautifulSoup(page.content,'html.parser')
            model_photos = soup.find_all('img',{'src':True})
            for i in model_photos:
                if i.has_attr('alt'):
                    if 'photo' not in i['alt']:
                        if i.has_attr('src'):
                            image = i['src']
                            if checker in image:
                                title = image.rsplit('_', 1)[1]
                                img_data = requests.get(image).content
                                folder_dir = f'{directory}/photos/{name}'
                                if os.path.exists(folder_dir):
                                    pass
                                else:
                                    os.makedirs(folder_dir)
                                try:
                                    with open(f'{folder_dir}/{title}.jpg','wb') as handler:
                                        handler.write(img_data)
                                except IsADirectoryError:
                                    pass
    # create pdf with the images                             
    file_names = os.listdir(folder_dir)
    images = [ Image.open(f'{folder_dir}/{f}') for f in file_names]
    pdf_path = f"{folder_dir}/{name}.pdf"
    images[0].save( pdf_path, "PDF" ,resolution=100.0, save_all=True, append_images=images[1:])

    print(f'🧲[green] Scraping {name} albums done. Images and PDF downloaded[/green]')

if 'playlist' in url:
    playlist()
elif 'photos' in url:
    photos()
elif 'pornstar' in url:
    pornstar()
else:
    video()
