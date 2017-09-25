import os, os.path as osp
import glob


def walk_directory(path, ext=None, ignore_dir=None):
    for dirname, dirnames, filenames in os.walk(path):
        for filename in filenames:
            if ext is None or filename.split(".")[-1].lower() in ext:
                # fpath = osp.join(dirname, filename)
                yield dirname, filename


if __name__ == "__main__":
    for t in walk_directory("."):
        print(t)
