import random
import string
from PIL import Image

def bw_image(new_image):
    img = Image.open(new_image)
    black_and_white = img.convert('L')
    letters = string.ascii_lowercase
    image_name = ''.join(random.choice(letters) for i in range(10))
    black_and_white.save('out_images/' +  image_name + '.png')
    black_and_white.show()

bw_image('image2.png')