import os

dir = './images'

i = 1
for image in os.listdir(dir):
    os.rename(f'{dir}/{image}', f'{dir}/{str(i).zfill(4)}.jpg')
    i += 1
