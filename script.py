import cv2
import numpy as np
import requests
from PIL import Image
from io import BytesIO
from collections import Counter, defaultdict

# URL da imagem
url = "https://privaliamarketplace.conectala.com.br/app/assets/images/product_image/E4543697-A509-C5A0-32B7-DF469BAB33FF/8de32abfcfaeabd781cc405b67393a7c/17193200661083.jpg"
#url = "https://privaliamarketplace.conectala.com.br/app/assets/images/product_image/7917ED9E-BCDF-D28C-3A1C-D6EBA4615968/17193238620709.jpg"
#url = "https://down-br.img.susercontent.com/file/d96ddb7aab30f967d5022d0951b6a016_tn"
#url = "https://cea.vtexassets.com/arquivos/ids/58655533/Foto-0.jpg?v=638515655362600000"

# Lista de cores principais com seus valores RGB
colors = {
    'Vermelho': (255, 0, 0),
    'Verde': (0, 255, 0),
    'Azul': (0, 0, 255),
    'Amarelo': (255, 255, 0),
    'Ciano': (0, 255, 255),
    'Rosa': (255, 192, 203),
    'Roxo': (128, 0, 128),
    'Marrom': (165, 42, 42),
    'Branco': (255, 255, 255),
    'Preto': (0, 0, 0),
    'Cinza': (128, 128, 128),
    'Laranja': (255, 165, 0),
    'Turquesa': (64, 224, 208),
    #'Prata': (192, 192, 192),
    'Ouro': (255, 215, 0)
}

# Função para encontrar a cor principal mais próxima
def closest_color(requested_color):
    min_distance = float('inf')
    closest_color_name = None
    for color_name, color_value in colors.items():
        r_c, g_c, b_c = color_value
        rd = (int(r_c) - int(requested_color[0])) ** 2
        gd = (int(g_c) - int(requested_color[1])) ** 2
        bd = (int(b_c) - int(requested_color[2])) ** 2
        distance = rd + gd + bd
        if distance < min_distance:
            min_distance = distance
            closest_color_name = color_name
    return closest_color_name

# Carregar a imagem da URL
response = requests.get(url)
img = Image.open(BytesIO(response.content))

# Converter a imagem para formato que o OpenCV pode trabalhar
img_cv = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)

# Redimensionar a imagem para facilitar a análise
height, width, _ = img_cv.shape
new_height = 400
new_width = int((new_height / height) * width)
resized_img = cv2.resize(img_cv, (new_width, new_height))

# Definir a região central da imagem
center_x, center_y = new_width // 2, new_height // 2
region_size = 100  # tamanho da região central
top_left_x = max(0, center_x - region_size // 2)
top_left_y = max(0, center_y - region_size // 2)
bottom_right_x = min(new_width, center_x + region_size // 2)
bottom_right_y = min(new_height, center_y + region_size // 2)

central_region = resized_img[top_left_y:bottom_right_y, top_left_x:bottom_right_x]

# Converter a imagem redimensionada para RGB
central_region_rgb = cv2.cvtColor(central_region, cv2.COLOR_BGR2RGB)

# Converter a imagem em uma lista de cores
pixels = central_region_rgb.reshape((-1, 3))

# Contar a frequência de cada cor
color_counts = Counter([tuple(map(int, color)) for color in pixels])

# Calcular a porcentagem de cada cor
total_pixels = sum(color_counts.values())
common_colors_percentage = [(color, count / total_pixels * 100) for color, count in color_counts.items()]

# Consolidar as cores principais
color_consolidation = defaultdict(float)
for color, percentage in common_colors_percentage:
    color_name = closest_color(color)
    color_consolidation[color_name] += percentage

# Ordenar e mostrar as 5 cores mais comuns, suas porcentagens
sorted_colors = sorted(color_consolidation.items(), key=lambda x: x[1], reverse=True)[:5]

for color_name, percentage in sorted_colors:
    print(f"Cor: {color_name}, Porcentagem: {percentage:.2f}%")
