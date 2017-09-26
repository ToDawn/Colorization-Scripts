import os, os.path as osp
import glob

from scipy.misc import imresize, imread, imsave



def walk_directory(path, ext=None, ignore_dir=None):
    for dirname, dirnames, filenames in os.walk(path):
        for filename in filenames:
            if ext is None or filename.split(".")[-1].lower() in ext:
                # fpath = osp.join(dirname, filename)
                yield dirname, filename




def resize_directory(origin_dir, output_dir, ratio=0.15):
    files = [_ for _ in walk_directory(origin_dir, ext="jpg")]

    for dname, fname in files:
        print(dname, fname)
        fpath = osp.join(dname, fname)
        img = imread(fpath)
        img = imresize(img, ratio)

        opath = osp.join(output_dir, fname)
        imsave(opath, img)

if __name__ == "__main__":
    origin_dir = "/home/ligeng/Documents/NUS_Color/Canon1DsMkIII_JPG"
    output_dir = "/home/ligeng/Documents/NUS_Color/Canon1DsMkIII_JPG_scale_15"
    resize_directory(origin_dir, output_dir)