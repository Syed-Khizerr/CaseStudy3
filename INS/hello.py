import hashlib

message = input("Enter a message to hash:").encode()
hashed_msg = hashlib.sha256(message).hexdigest()

print(message)
print(hashed_msg)