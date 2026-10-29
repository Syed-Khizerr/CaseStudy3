from cryptography.hazmat.primitives.asymmetric import dsa
from cryptography.hazmat.primitives import hashes
from cryptography.exceptions import InvalidSignature

private_key = dsa.generate_private_key(key_size=2048)
public_key = private_key.public_key()

print("DSA key pair generated successfully.")

message = b"Digital Signature Standard"
signature = private_key.sign(message, hashes.SHA256())

print("\nOriginal Message:")
print(message.decode())

print("\nDigital Signature:")
print(signature.hex())

try:
    public_key.verify(signature, message, hashes.SHA256())
    print("\nSignature Verification:")
    print("Signature is VALID.")

except InvalidSignature:
    print("\nSignature Verification:")
    print("Signature is INVALID.")

modified_message = b"Digital Signature Standard Modified"

try:
    public_key.verify(signature, modified_message, hashes.SHA256())
    print("\nModified Message Verification:")
    print("Signature is VALID.")

except InvalidSignature:
    print("\nModified Message Verification:")
    print("Signature is INVALID.")