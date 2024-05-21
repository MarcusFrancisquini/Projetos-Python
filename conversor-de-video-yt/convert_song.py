# pip install pytube
import os
from pytube import YouTube

# link do vídeo
yt = YouTube(str(input('Entre com a URL do vídeo \n>> ')))

# processando o vídeo
video = yt.streams.filter(only_audio=True).first()

# salvando o arquivo
print('Onde deseja salvar o arquivo? (deixe em branco para salvar no diretório atual)')
outputPath = str(input('>> ')) or '.'
outFile = video.download(output_path=outputPath)

# convertendo o arquivo
base, ext = os.path.splitext(outFile)
newFile = base + '.mp3'
os.rename(outFile, newFile)
print(yt.title + ' foi baixado com sucesso!')
