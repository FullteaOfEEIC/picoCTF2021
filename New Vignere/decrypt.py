import subprocess
import string
from multiprocessing import Pool, cpu_count
from tqdm import tqdm

ALPHABET = string.ascii_lowercase[:16]
subprocess.call(["g++", "-Wall", "-Ofast", "-o", "vig", "decrypt.cpp"])

def run(d):
    seed_min = d[0]
    seed_max = d[1]
    subprocess.call(["./vig", str(seed_min), str(seed_max)])


batch_size = len(ALPHABET)**13 // (cpu_count() * (16**5))
seeds = [(i, i + batch_size) for i in range(1, len(ALPHABET) ** 10, batch_size)]  # try keys whose length are <10


if __name__ == '__main__':
    with Pool() as p:
        imap = p.imap(run, seeds)
        list(tqdm(imap, total=len(seeds)))
