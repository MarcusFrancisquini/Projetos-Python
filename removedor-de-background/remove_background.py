# pip install rembg
# pip install Pillow
from rembg import remove
from PIL import Image

img_entrada = 'robot.png'

# formato de saída da imagem deve ser .PNG
img_saida = 'output.png'

inputimage = Image.open(img_entrada)
output = remove(inputimage)

output.save(img_saida)
