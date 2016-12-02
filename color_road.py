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
        print('This image is: ', type(self.image),
              'with dimensions:', self.image.shape)

    def copy__image(self):
        xsize = self.image.shape[0]
        ysize = self.image.shape[1]
        color_select = np.copy(self.image)
        print(color_select)

    def generate__image(self):
        red_threshold = 225
        green_threshold = 100
        blue_threshold = 100
        rgb_threshold = [red_threshold, green_threshold, blue_threshold]
        color_select = np.copy(self.image)
        # Use a "bitwise OR" to identify pixels below the threshold
        thresholds = (self.image[:, :, 0] < rgb_threshold[0]) | (self.image[:, :, 1] < rgb_threshold[1]) | (self.image[:, :, 2] < rgb_threshold[2])

        color_select[thresholds] = [0, 0, 0]
        # Display the image
        plt.imshow(color_select)
        plt.show()


test = Main('test.jpg')
test.generate__image()
