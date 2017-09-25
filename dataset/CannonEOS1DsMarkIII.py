import os
import os.path as osp
data = {
    "raw" : [
        'http://www.comp.nus.edu.sg/~whitebal/illuminant/files/Canon1DsMkIII_RAW.zip.001',
        'http://www.comp.nus.edu.sg/~whitebal/illuminant/files/Canon1DsMkIII_RAW.zip.002',
        'http://www.comp.nus.edu.sg/~whitebal/illuminant/files/Canon1DsMkIII_RAW.zip.003',
        'http://www.comp.nus.edu.sg/~whitebal/illuminant/files/Canon1DsMkIII_RAW.zip.004',
        'http://www.comp.nus.edu.sg/~whitebal/illuminant/files/Canon1DsMkIII_RAW.zip.005',
    ],

    "jpeg" : [
        'http://www.comp.nus.edu.sg/~whitebal/illuminant/files/Canon1DsMkIII_JPG.zip.001',
        'http://www.comp.nus.edu.sg/~whitebal/illuminant/files/Canon1DsMkIII_JPG.zip.002',
    ],
    "png" : [
        'http://www.comp.nus.edu.sg/~whitebal/illuminant/files/Canon1DsMkIII_PNG.zip.001',
        'http://www.comp.nus.edu.sg/~whitebal/illuminant/files/Canon1DsMkIII_PNG.zip.002',
        'http://www.comp.nus.edu.sg/~whitebal/illuminant/files/Canon1DsMkIII_PNG.zip.003',
        'http://www.comp.nus.edu.sg/~whitebal/illuminant/files/Canon1DsMkIII_PNG.zip.004',
    ],

    "mask" : [
        'http://www.comp.nus.edu.sg/~whitebal/illuminant/files/Canon1DsMkIII_CHECKER.zip'
    ],

    "mat" : [
        'http://www.comp.nus.edu.sg/~whitebal/illuminant/files/Canon1DsMkIII_gt.mat'
    ]
}

def download(root, url):
    fname = root
    if not osp.exist(fname):
        os.makedirs(fname)

if __name__ == "__main__":
    pass
    # import inspect, os
    # fname = inspect.getfile(inspect.currentframe()) ).strip().split(".")[0]
    #
    #
    #
    # for key, value in data.items():
