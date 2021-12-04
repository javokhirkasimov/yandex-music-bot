from yandex_music import Client
import os

def search_music(music_name):
    client = Client.from_credentials('yandex-music-login','password')    
    search_result = client.search(music_name)
    print(search_result)
    if search_result.best:

        type_ = search_result.best.type
        best = search_result.best.result
        print(type_)            
        if type_ == 'track':
            if best.artists:
                artists = ""
                artists = ' - ' + ', '.join(artist.name for artist in best.artists)
            return search_result.best.result.download(filename=f"./musics/{best.title + artists}.mp3")
        elif type_ == 'artist':
            return {"artist":best.name}
        elif type_ in ['album', 'podcast']:
            return {"album":best.title}
        elif type_ == 'playlist':
                return {"playlist":best.title}
        else:
            return 'Non' 
    else:
        return 'Non'


def download_world_tracks(CHART_ID,user_id):
    client = Client.from_credentials('yandex-music-login','password')
    world_chart = client.chart(CHART_ID).chart
    musics_path = f'./musics/{CHART_ID}/{user_id}/'
    os.mkdir(musics_path)
    count = 0
    for m in world_chart.tracks:
        count += 1
        print(f'{m.chart.position}-{m.track.title}')
        artists = ""
        artists = ' - ' + ', '.join(artist.name for artist in m.track.artists)
        m.track.download(filename=f'{musics_path}{m.track.title}{artists}.mp3')
        if count == 10:
            return
