import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import argparse
from tools.ImageReader import *
from skimage import io


def parse_args():
    desc = "Anutomatic Coloring"
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument('--path', type=str, default='./data/test_img.jpg', help='The path of the file')

    return parser.parse_args()


def find_edge(img):
    color = [25,25,25]
    result = np.all(img <= color, axis=-1)
    return result

def find_color(img):
    color = [245,245,245]
    return np.all(img<color,axis=-1)


def classify(img,color,rad = 2):
    colormap = np.ones
    colorset = {}
    #store color with index and color.
    for i in range(len(color)):
        for j in range(len(color[i])):
            if color[i][j] == True:
                print(img[i][j])
                if colorset.get(img[i][j])!= None:
                    colorset[img[i][j]] = (i,j)
    return colorset

def compare_color(color1, color2,diff):
    compare = []
    for i in range(len(color1)):
        compare[i] = np.absolute(color1[i]-color2[i])
    for i in compare:
        if i>diff:
            return False
    return True



def main():
    args = parse_args()
    # img = mpimg.imread(args.path)
    #Read IMG
    img = io.imread(args.path)
    #Get Edge
    edge = find_edge(img)
    print(edge)

    #remove Edge
    img[edge] = [255,255,255]
    plt.imshow(img)
    plt.show()


    color = find_color(img)
    block = classify(img,color)


    # find_overlap()
    # generate()


if __name__ == '__main__':
    main()
