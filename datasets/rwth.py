import os
from glob import glob

import torch
from torch.utils.data import Dataset
import pandas as pd

from PIL import Image

class RWTHAllImg(Dataset):
    """Class to load all images from RWTH dataset"""
    def __init__(self, globpattern, transform=None):
        self.imglobs = globpattern
        self.transform = transform
    
    def __getitem__(self, idx):
        if torch.is_tensor(idx):
            idx = idx.tolist()
        img = Image.open(self.imglobs[idx])
        if self.transform:
            img = self.transform(img)
        sample = {'image': img}
        return sample
    
    def __len__(self):
        return len(self.imglobs)

class RWTHSignDataset(Dataset):
    """RWTH Phoenix dataset"""
    def __init__(self, csv_file, sign_dir, transform=None):
        df = pd.read_csv(csv_file, delimiter='|')
        self.sign_dir = sign_dir
        sign_folders = list(df['folder'])
        self.annotations = df['annotation']
        self.frame_files = [sorted(glob(os.path.join(self.sign_dir, f))) for f in sign_folders]
        self.transform = transform

    def __len__(self):
        return len(self.annotations)

    def __getitem__(self, idx):
        if torch.is_tensor(idx):
            idx = idx.tolist()
        frames = [Image.open(f) for f in self.frame_files[idx]]
        if self.transform:
            frames = [self.transform(f) for f in frames]
        #sample = {'frames': frames, 'annotations': self.annotations[idx]}

        return frames, self.annotations[idx]
