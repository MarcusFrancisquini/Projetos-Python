# pip install pillow
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

textos = ['Notebook Branco', 'Work Time!']

contador = 1
for n in textos:

    imagem = Image.open('computador.png')

    draw = ImageDraw.Draw(imagem)

    # fonte que será utilizada
    font = ImageFont.truetype('ALGER.TTF', 90)

    # posição do texto na imagem
    draw.text((121, 77), n, font=font)

    imagem.save(f'imagem{contador}.png')
    contador += 1

