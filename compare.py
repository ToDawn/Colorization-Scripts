import os, os.path as osp

import numpy as np
from PIL import Image

from common import walk_directory

IMG_EXTENSION = ["jpg"]
eps = 1e-8

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
    img1 = Image.open(img_path1)
    img2 = Image.open(img_path2)

    # resize to keep same
    w, h = img1.size
    img2 = img2.resize((w, h), Image.ANTIALIAS)

    # to numpy
    img1 = np.array(img1, dtype=np.float)
    img2 = np.array(img2, dtype=np.float)

    # gamma?

    img1 = img1.reshape(-1, 3)
    img2 = img2.reshape(-1, 3)

    result = []

    for row in range(img1.shape[0]):
        res = np.dot(img1[row], img2[row].T) / (np.linalg.norm(img1[row]) * np.linalg.norm(img2[row]) + eps)
        angle = np.arccos(res)
        result.append(angle)

    return result


def test_all_images(path1, path2):
    files = find_test_images(path1, path2)

    result = []

    for f in files:
        ipath1 = osp.join(path1, f)
        ipath2 = osp.join(path2, f)

        temp_res = test_single_image(ipath1, ipath2)
        result.append(temp_res)

        print(f, np.mean(temp_res))

    return result


if __name__ == "__main__":
    pass
