import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np


class Main:
    image = None

    def __init__(self, image_path):
        self.read__image(image_path)
        pass

    def read__image(self, image_path):
        self.image = mpimg.imread(image_path)
        print('this image is : ', type(self.image))


test = Main('test.jpg')
