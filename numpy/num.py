import numpy as np
from PIL import Image
file_path='lunar03_raw.jpg'
# считаем картинку в numpy array
img = Image.open(file_path)
data = np.array(img)
# ... логика обработки
updated_data=(data-data.min())*int(255/(data.max()-data.min()))

# запись картинки после обработки
res_img = Image.fromarray(updated_data)
res_img.save('lunar03.jpg')