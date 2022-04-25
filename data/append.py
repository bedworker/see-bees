import os

dir = './images'

with open(f'{dir}/train.csv', 'a') as fp:
    for image in sorted(os.listdir(dir)):
        if(image.endswith('.jpg')):
            fp.write(f'\n{image}')