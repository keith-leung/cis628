from collections import Counter
import random
import sys

# Build a customized full character range of CJK chars
## 1. Read all the chars into a dictionary
## 2. Shuffle all the key to a list, and this list will be the whole set of chars and a part of the key
## 3. Calculate the freequency of each char which is in the char space, and keep the relation of char:count
## 4. shuffle char:count as the key as char:shift, which means the char i shift j
## 5. Safe the two parts of the key, which is whole char space and the char:shift relations
## 6. When the article comes again
### 6.1 Replace all the sensitive keywords with Aho-Corasick algorithm
### 6.2 Iterate all the chars, if a char c is in the char space, then shift cj in the char space, and get the char
### 6.3 Replace the c with cj in the article
## 7. When decryption comes
### 7.1 Iterate all the chars, if a char d is in the char space, then shift negative j as dj in the char space, and get the char
### 7.1 Replace the d with dj in the article


def generate_key(dic_cjk, plainText):
    for line in plainText:
        for c in line:
            if c in dic_cjk.keys():
                dic_cjk[c] += 1

    key_space_range = len(dic_cjk.keys())
    key_set = {}
    for key in dic_cjk.keys():
        if dic_cjk[key] > 0:
            # shift number of occurrence plus a random number
            key_set[key]= (dic_cjk[key] + random.randint(0, key_space_range)) % key_space_range

    return key_set

def encrypt(key_set, dic_cjk, plainText):
    # sort_key_cjk
    key_table = sorted(dic_cjk.keys())
    length = len(key_table)
    indexed_key_table = {}
    current = 0
    for k in key_table:
        indexed_key_table[k] = current
        current += 1

    cipherText = ''
    cipherMap = {}

    for line in plainText:
        for c in line:
            if c in key_set.keys():
                shift = key_set[c]
                originPlace = indexed_key_table[c]
                shifted_char_index = (originPlace + shift) % length
                shifted_char = key_table[shifted_char_index]
                cipherMap[shifted_char] = shift
                cipherText += shifted_char
            else:
                # do not change
                cipherText += c

    cipherTableMap = []
    for item in key_table:
        if item in cipherMap.keys():
            cipherTableMap.append((item, cipherMap[item]))
        else:
            cipherTableMap.append((item,0))

    return cipherText, cipherTableMap


def decrypt(key_table, cipherText):
    plainText = ''
    length = len(key_table)
    cipherMap = {}
    for item in key_table:
        cipherMap[item[0]] = item[1]
    codeTablePosition = {}
    current = 0
    for item in key_table:
        codeTablePosition[item[0]] = current
        current += 1

    for line in cipherText:
        for c in line:
            if c in cipherMap.keys():
                shift = cipherMap[c]
                codePosition = codeTablePosition[c]
                shifted_place = codePosition - shift
                if shifted_place < 0:
                    shifted_place += length
                shifted_char = key_table[shifted_place][0]
                #print(shifted_char)
                plainText += shifted_char
            else:
                # do not change
                plainText += c

    return plainText
