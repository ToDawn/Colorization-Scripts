
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


def test_single_image(path1, path2):
    img1 = np.array(Image.open(path1))
    img2 = np.array(Image.open(path2))

    # gamma?

    img1 = img1.reshape(-1, 3)
    img2 = img2.reshape(-1, 3)

    all_result = []

    for row in range(img1.shape[0]):
        res = img1[row] * img2[row].T
        all_result.append(res)

    return all_result



if __name__ == "__main__":
    pass
