# Python program to find SHA256 hash string of a file
import hashlib
import os

dir_name='C:/praveen/input_sample/'
filename = 'gethash.py'
fileh = os.path.join(dir_name, filename)
print(fileh)
sha256_hash = hashlib.sha256()
with open(fileh ,"rb") as f:
    # Read and update hash string value in blocks of 4K
    for byte_block in iter(lambda: f.read(4096),b""):
        sha256_hash.update(byte_block)
    print(sha256_hash.hexdigest())