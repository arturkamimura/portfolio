from PIL import Image
from glob import glob

imagens = glob('*.jpg') + glob('*.png')

for imagem in imagens:

    # Abre a imagem
    img = Image.open(imagem)

    # Redimensiona a imagem para 800x600
    img_resized = img.resize((600, 400))

    # Salva a imagem redimensionada
    img_resized.save(imagem)