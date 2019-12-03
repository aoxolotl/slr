import os, sys
from glob import glob
import pandas as pd
from tqdm import tqdm

if __name__ == "__main__":

    base_dir = "/home/reverie/datasets/phoenix2014-release/phoenix-2014-multisigner"

    csvf = "annotations/manual/train.corpus.csv"
    csvf = os.path.join(base_dir, csvf)
    imdir = "features/fullFrame-210x260px/train/"
    outf = 'signrates.csv'
    
    # ID|FOLDER|SIGNER|ANNOTATION(GLOSS)
    df = pd.read_csv(csvf, delimiter='|')

    sign_rate = []
    with open(outf, 'w') as f:
        for i, d in tqdm(df.iterrows()):
            #print(d)
            impath = os.path.join(base_dir, imdir, d['folder'])
            num_ims = len(glob(impath))
            num_signs = len(d['annotation'].split())
            rate = num_ims / num_signs
            if rate > 1.0 and rate < 50:
                sign_rate.append(rate)
            f.write(f"{impath}|{num_ims}|{num_signs}|{rate}\n")

        avg_rate = sum(sign_rate) / len(sign_rate)
        max_rate = max(sign_rate)
        min_rate = min(sign_rate)
        print("max:{}, min:{}, avg:{}".format(\
              max_rate, min_rate, avg_rate))
        f.write(f"max:{max_rate}, min:{min_rate}, avg:{avg_rate}")


