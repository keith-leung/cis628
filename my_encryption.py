import os
import uuid
import yaml
import json
import custom_cjk_vigenere_cipher
import my_utils
from NTRU_python.NTRU.NTRUencrypt import NTRUencrypt
from NTRU_python.NTRU.NTRUdecrypt import NTRUdecrypt
from NTRU_python.NTRU.NTRUutil import *

'''
Generate 2 Lattice keys, then use a lattice private key and one lattice public key as Key A, and Key B
We can consider Key A and Key B are both public or private key
'''


def key_pair_generation(keyAfilePath='', keyBfilePath=''):
    if keyAfilePath == '':
        # generate and return in memory
        keys = generate_one()
        return keys
    elif keyBfilePath == '':
        # return one as the memory key
        keys = generate_one()
        keyB = keys[-1]
        save_to_file(keyAfilePath, keys[0])
        return [keyB]
    else:
        # Both return as files, then nothing to return as a list
        keys = generate_one()
        save_to_file(keyAfilePath, keys[0])
        save_to_file(keyBfilePath, keys[-1])
        return []


'''
'''
def encrypt(keyLattice, plainText):
    '''
    :param keyLattice:
    :param plainText:
    :return:
    '''
    ## 1. generate Vigenere cipher key by content, which is considered as randomness
    ## 2. Vigenere cipher with this key
    ## 3. Lattice encrypt the Vigenere cipher key
    ## 4. Pack the cipher text and encrypted key to a file
    dic_cjks = read_all_cjk_chars_from_config()
    key_for_custom_v = custom_cjk_vigenere_cipher.generate_key(dic_cjks, plainText)
    cipher_text, codetable = custom_cjk_vigenere_cipher.encrypt(key_for_custom_v, dic_cjks, plainText)

    E = NTRUencrypt()
    # And read the public key
    #E.readPub('keyLattice' + ".pub")
    E.readPub(keyLattice)
    str_key_for_custom_v = json.dumps(codetable)

    #DEBUG MODE
    if my_utils.is_debug_mode():
    #E.encryptString(str_key_for_custom_v)
        print('DEBUG MODE: Lattice-based encryption is skipped')
        encrypted_lattice_key = str_key_for_custom_v
    else:
        E.encryptString(str_key_for_custom_v)
        encrypted_lattice_key = E.Me
    # END DEBUG
    # str_code_table = json.dumps(codetable)

    result = cipher_text + '\r' + '-----BEGIN LATTICE PRIVATE KEY-----' + '\r' + encrypted_lattice_key \
             + '\r' + '-----END LATTICE PRIVATE KEY-----' #+ '\r' + str_code_table

    return result


'''
'''
def replace_sensitive(text):
    file_names = []
    with open("config.yaml", "r") as yamlfile:
        data = yaml.load(yamlfile, Loader=yaml.FullLoader)
        for key, value in data.items():
            if key == 'Sensitive':
                print(key, ":", value)
                file_names = value

    sensitive_dict = {}
    for f in file_names:
        with open('data/' + f, encoding="utf8") as file:
            content = file.readlines()
            for line in content:
                if line.__contains__('|'):
                    splited = line.split('|')
                    sensitive_dict[splited[0].strip()] = splited[1].strip()
                else:
                    word = line.strip()
                    sensitive_dict[word] = '*' * len(word)

    from py_aho_corasick import py_aho_corasick

    # keywords only
    A = py_aho_corasick.Automaton(list(sensitive_dict.keys()))

    #A = py_aho_corasick.Automaton(['透视眼', '透视', '透视镜'])
    text2 = []
    for line in text:
        results = A.get_keywords_found(line)
        results = results[::-1]
        for idx, k, v in results:
            line = line[:idx] + sensitive_dict[k] + line[idx+len(k):]
        text2.append(line)

    return text2


def decrypt(keyLattice, cipherText):
    '''
    :param keyLattice:
    :param cipherText:
    :return:
    '''
    ## 1. Read sections from cipher text
    ## 2. Decrypt Vigenere cipher with Lattice key
    ## 3. Decrypt encrypted cipher section Vigenere cipher key
    ## 4. return plain text

    if cipherText.__contains__('-----BEGIN LATTICE PRIVATE KEY-----') \
        and cipherText.__contains__('-----END LATTICE PRIVATE KEY-----') :
        pass
    else:
        return cipherText

    cipherSection = cipherText.split('\r-----BEGIN LATTICE PRIVATE KEY-----\r')[0]
    keySection = cipherText.split('\r-----BEGIN LATTICE PRIVATE KEY-----\r')[1].split('\r-----END LATTICE PRIVATE KEY-----')[0]
    #codeTableSection = cipherText.split('\r-----BEGIN LATTICE PRIVATE KEY-----\r')[1].split('\r-----END LATTICE PRIVATE KEY-----\r')[1]

    #dic_cjks = json.loads(codeTableSection)

    D = NTRUdecrypt()
    # And read the public key
    D.readPriv(keyLattice +".priv")
    # DEBUG Mode
    if my_utils.is_debug_mode():
        print('DEBUG MODE: Lattice-based decryption is skipped')
        key_for_custom_v = keySection
    else:
        D.decryptString(keySection)
        key_for_custom_v = D.M
    # END DEBUG mode
    key_table = json.loads(key_for_custom_v)
    plain_text = custom_cjk_vigenere_cipher.decrypt(key_table, cipherSection)
    return plain_text


def unbox_key_lattice(cipherText):
    lines = cipherText.split('\n')

    to_decrypt = ''
    key_for_lattice = ''
    for l in lines:
        if l == '-----BEGIN LATTICE PRIVATE KEY-----':
            break

    pass


def generate_one():
    N1 = NTRUdecrypt()
    N1.setNpq(N=107, p=3, q=64, df=15, dg=12, d=5)
    random_key_name1 = str(uuid.uuid1())
    random_key_name2 = str(uuid.uuid1())
    N1.genPubPriv(random_key_name1)
    N1.genPubPriv(random_key_name2)

    keyA = ''
    keyB = ''

    # read both
    with open(random_key_name1 + '.priv') as file:
        df = read_to_end(file.read())
        print(df)
        keyA = df + '\n' + '-----BEGIN LATTICE-----' + '\n'
    with open(random_key_name2 + '.priv') as file:
        df = read_to_end(file.read())
        print(df)
        keyB = df + '\n' + '-----BEGIN LATTICE-----' + '\n'
    with open(random_key_name1 + '.pub') as file:
        df = read_to_end(file.read())
        print(df)
        keyB += df
    with open(random_key_name2 + '.pub') as file:
        df = read_to_end(file.read())
        print(df)
        keyA += df

    delete_files([random_key_name1 + '.priv', random_key_name2 + '.priv',
                  random_key_name1 + '.pub', random_key_name2 + '.pub'])

    return [keyA, keyB]


def read_all_cjk_chars_from_config():
    file_names = []
    with open("config.yaml", "r") as yamlfile:
        data = yaml.load(yamlfile, Loader=yaml.FullLoader)
        for key, value in data.items():
            if key == 'CJK':
                print(key, ":", value)
                file_names = value

    cjk_dict = {}
    for f in file_names:
        with open('data/' + f, encoding="utf8") as file:
            content = file.readlines()
            for c in content:
                if c is not None and c != '' and c.strip() != '':
                    char = c.strip()
                    cjk_dict[char] = 0

    return cjk_dict


def read_to_end(file):
    str_return = ''
    for line in file:
        print(line)
        str_return += line
    return str_return


def delete_files(filePaths):
    for f in filePaths:
        delete_file(f)


def delete_file(file_path):
    # checking if file exist or not
    if os.path.isfile(file_path):
        # os.remove() function to remove the file
        os.remove(file_path)
        # Printing the confirmation message of deletion
        print("File Deleted successfully")
    else:
        print("File does not exist")
    # Showing the message instead of throwig an error


def save_to_file(keyAfilePath, content):
    with open(keyAfilePath, 'w') as file:
        file.write(content)
    pass
