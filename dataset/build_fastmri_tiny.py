

'/media/NAS03/fastMRI/knee/d.2.0.complex.sc/train/PD/h5'



from glob import glob
import os
import h5py

def mkdir(path):
    if not os.path.exists(path):
        os.makedirs(path)


if __name__ == '__main__':
    path = '/media/NAS03/fastMRI/knee/d.2.0.complex.sc/train/PD/h5'
    files = glob(os.path.join(path, '*.h5'))