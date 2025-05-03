import hashlib
# print(hashlib.algorithms_available)
# print(hashlib.algorithms_guaranteed)

hash_object = hashlib.blake2b(b'Hello World')
print(hash_object.hexdigest())
hash_object = hashlib.sha512(b'Hello World')
print(hash_object.hexdigest())