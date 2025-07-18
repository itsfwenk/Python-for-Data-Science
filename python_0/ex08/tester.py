from time import sleep
from tqdm import tqdm
from Loading import ft_tqdm
import time


for elem in ft_tqdm(range(333)):
    sleep(0.005)
print()

for elem in tqdm(range(333)):
    sleep(0.005)
print()

print("Starting download...", end='', flush=True)
time.sleep(2)
print("Done!")