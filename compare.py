import os, os.path as osp

import numpy as np
from PIL import Image

from common import walk_directory

IMG_EXTENSION = ["jpg"]


def normalize(img):
    """
    Normalize img from 0~255 to 0~1
    :param img:
    :return:
    """
    pass


def find_test_images(path1, path2, extension=IMG_EXTENSION):
    l1 = list(walk_directory(path=path1, ext=extension))
    l2 = list(walk_directory(path=path2, ext=extension))

    s1 = set([_[1] for _ in l1])
    s2 = set([_[1] for _ in l2])

    return list(s1 & s2)


def test_single_image(img_path1, img_path2):
    img1 = np.array(Image.open(img_path1))
    img2 = np.array(Image.open(img_path2))

    # gamma?

    img1 = img1.reshape(-1, 3)
    img2 = img2.reshape(-1, 3)

    result = []

    for row in range(img1.shape[0]):
        res = img1[row] * img2[row].T
        result.append(res)

    return result


def test_all_images(path1, path2):
    files = find_test_images(path1, path2)

    result = []

    for f in files:
        ipath1 = osp.join(path1, f)
        ipath2 = osp.join(path2, f)

        result.append(test_single_image(ipath1, ipath2))

    return result


if __name__ == "__main__":
    pass
