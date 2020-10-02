import pytube
import PySimpleGUI as pg


layout = [
    [pg.Text('Video source'), pg.InputText(), pg.Submit()]
]
window = pg.Window('YT_downloader', layout)
while True:
    event, values = window.read()
    if event in (None, 'Exit'):
        break
    if event == pg.Submit():
        print(pg.InputText())
    yt = pytube.YouTube(str(values))
    stream = yt.streams.first()
    stream.download('D:\github\YT_downloader')
window.close()   