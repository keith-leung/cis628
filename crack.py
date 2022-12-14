from binascii import hexlify, unhexlify
from Crypto.Cipher import AES

list_keys = []
with open("keys.out",  'r', encoding='utf8') as f:
    while True:
        line = f.readline()
        if not line:
            break
        list_keys.append(line.strip())
print(list_keys)

found = False
result = 'd06bf9d0dab8e8ef880660d2af65aa82'
for one in list_keys:
    key = unhexlify(one)
    # key = unhexlify('2b7e151628aed2a6abf7158809cf4f3c')
    IV = unhexlify('09080706050403020100A2B2C2D2E2F2')
    plaintext1 = unhexlify('255044462d312e350a25d0d4c5d80a34')
    cipher = AES.new(key, AES.MODE_CBC, IV)
    ciphertext = hexlify(cipher.encrypt(plaintext1)).decode()

    print('hexlify cipher:' + ciphertext)
    if str(ciphertext).casefold() == result.casefold():
        print('result found: ' + one)
        found = True
        break


if not found:
    print('not found!! ')









"""

    '''
    decipher = AES.new(key,AES.MODE_CBC,IV)
    plaintext = decipher.decrypt(ciphertext)
    print('hexlify plaintext:' + str(hexlify(plaintext)))
    print('------------------------------')'''

iv = "09080706050403020100A2B2C2D2E2F2"




password = "93c4ad2033792205fb2a29d1dc7c4f50"
msg = "255044462d312e350a25d0d4c5d80a34"

print(f"IV: {iv}")
print(f"PWD: {password}")
print(f"MSG: {msg}")

# Convert Hex String to Binary
iv = unhexlify(iv)
password = unhexlify(password)

# Pad to AES Block Size
msg = pad(msg.encode(), AES.block_size)
# Encipher Text
cipher = AES.new(password, AES.MODE_CBC, iv)
cipher_text = cipher.encrypt(msg)
print(cipher_text)
print(b64encode(cipher_text).decode('ascii'))
# Encode Cipher_text as Base 64 and decode to String
out = b64encode(cipher_text).decode('utf-8')
print(f"OUT: {out}")

# Decipher cipher text
decipher = AES.new(password, AES.MODE_CBC, iv)
# UnPad Based on AES Block Size
plaintext = unpad(decipher.decrypt(b64decode(out)), AES.block_size).decode('utf-8')
print(f'PT: {plaintext}')
"""