import os
import numpy as np
from skimage import io


class ImageIO(object):

    def __init__(self, path):
        '''Variables :
            path_________________Path we want to read file from : Str
            '''

        self.path = path
        self.isDir = os.path.isdir(path)


    #Return RGBA images
    def readImgFromFile(self):
        return io.imread(self.path)
