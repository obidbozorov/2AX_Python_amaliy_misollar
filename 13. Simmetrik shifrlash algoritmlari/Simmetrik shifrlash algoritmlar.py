from Crypto.Cipher import DES,AES,Blowfish
key = b'-8B key-'
cipher = DES.new(key, DES.MODE_OFB, IV=b'12335679')
plaintext = b'Niyozmetov Dilshod'
print(cipher.iv)
msg = cipher.encrypt(plaintext)
print(type(msg))
print(msg.hex())
#print(msg.decode('utf-8').strip())
dmsg=cipher.decrypt(msg)
print("Deshifrlangan matn: ",dmsg)