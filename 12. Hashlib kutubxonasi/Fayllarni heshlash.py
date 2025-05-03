import hashlib
file = f"D:\\Instal\\Labaratoriya INSTAL\\ISO\\u_win_10_19045.4780_3in1_x64_by_AG_08.2024.iso"
BLOCK_SIZE = 65536
file_hash = hashlib.md5()
with open(file, 'rb') as f:
    fb = f.read(BLOCK_SIZE)
    while len(fb) > 0:
        file_hash.update(fb)
        fb = f.read(BLOCK_SIZE)

print (file_hash.hexdigest())
