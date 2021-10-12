from time import sleep
from yandex_music import Client

RUSSIA_ID='russia'
CHART_ID="world"
UZ_ID='uzbekistan'
client = Client.from_credentials('kasimovjavohir01@icloud.com','kasimov01')
world_chart = client.chart(CHART_ID).chart
ru_chart=client.chart(RUSSIA_ID).chart
uz_chart=client.chart(UZ_ID).chart


def download_world_tracks():
    musics_path = './musics/world/'
    count = 0
    for m in world_chart.tracks:
        count += 1
        print(f'{m.chart.position}-{m.track.title}')
        m.track.download(filename=f'{musics_path}{m.track.title}.mp3')
        sleep(1)
        if count == 10:
            return

def download_russia_tracks():
    musics_path = './musics/russia/'
    count = 0
    for m in ru_chart.tracks:
        count += 1
        print(f'{m.chart.position}-{m.track.title}')
        m.track.download(filename=f'{musics_path}{m.track.title}.mp3')
        sleep(1)
        if count == 10:
            return


def download_uzbek_tracks():
    musics_path = './musics/uzbek/'
    count = 0
    for m in uz_chart.tracks:
        count += 1
        print(f'{m.chart.position}-{m.track.title}')
        m.track.download(filename=f'{musics_path}{m.track.title}.mp3')
        sleep(1)
        if count == 10:
            return
