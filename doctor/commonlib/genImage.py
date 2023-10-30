import os

from PIL import Image

abs_path = os.path.abspath(__file__)



def create_image(origin_path, size):
    image_name = "img_{}.jpg".format(size)
    pri_image = Image.open(origin_path)
    pri_image.resize((size * 2, size), Image.ANTIALIAS).save(image_name)


if __name__ == "__main__":
    create_image("1024.jpg", 2700)