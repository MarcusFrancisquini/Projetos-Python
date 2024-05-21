# pip install rembg
# pip install Pillow
from rembg import remove
from PIL import Image

# informando a imagem
img_entrada = 'robot.png'
img_saida = 'output.png'

# processando a imagem
inputimage = Image.open(img_entrada)
output = remove(inputimage)

# salvando a imagem
output.save(img_saida)

# OBS: o formato de saída da imagem tem que ser .PNG
