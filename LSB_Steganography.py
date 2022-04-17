import numpy as np
import random
from skimage.io import imread, imsave
import pathlib



def encode(coverimg, data):
    img = imread(coverimg)
    startpoint = random.randint(0, img.shape[0] * img.shape[1] - 5 * 8 * 8)
    endpoint = startpoint + len(data) * 8
    linearimage = img.reshape(img.shape[0] * img.shape[1], img.shape[2])

    bt = "".join([bin(ord(i))[2:].zfill(8) for i in data])
    rorgorb = random.randint(0, 3)

    for i, bit in zip(range(startpoint, endpoint + 1), bt):
        if bit == "0" and linearimage[i][rorgorb] & 1 == 1:
            linearimage[i][rorgorb] = linearimage[i][rorgorb] - 1
        elif bit == "1" and linearimage[i][rorgorb] & 1 == 0:
            linearimage[i][rorgorb] = linearimage[i][rorgorb] + 1

    stegoimg = linearimage.reshape(img.shape[0], img.shape[1], img.shape[2])
    ext = pathlib.Path(coverimg).suffix
    imsave("stegoimg" + ext, stegoimg)

    return startpoint, endpoint, rorgorb


def decode(stegoimage, startpoint, endpoint, rorgorb):
    img = imread(stegoimage)
    linearimage = img.reshape(img.shape[0] * img.shape[1], img.shape[2])
    result = ""
    bitstring = ""
    count = 0
    for pixle in range(startpoint, endpoint + 1):

        if count == 8:
            result = result + chr(int(bitstring, 2))
            count = 0
            bitstring = ""
        if linearimage[pixle][rorgorb] & 1:
            bitstring = bitstring + '1'
        else:
            bitstring = bitstring + '0'
        count = count + 1

    return result









