import yaml
import argparse
import my_encryption
import my_utils
from NTRU_python.NTRU.NTRUdecrypt import NTRUdecrypt

def encrypt():
    pass

def decrypt():
    pass


def encrypt_and_decrypt_simple():
    '''
    1. read all configuration files
    2. encrypt data/SimpleText.txt
    3. make a copy of the result and show
    4. decrypt data/SimpleText.txt
    5. make a copy of the result and show
    :return:
    '''

    # read plain text
    plaintext = my_utils.read_to_end('data/SimpleText.txt')
    keyLattice = 'simple_key'
    N1 = NTRUdecrypt()
    N1.setNpq(N=167, p=3, q=128, df=61, dg=20, d=18)

    # Actually generate and save the public and private keys
    N1.genPubPriv(keyLattice)

    # debug
    N2 = NTRUdecrypt()
    N2.readPriv(keyLattice + ".priv")

    ciphertext = my_encryption.encrypt(keyLattice + ".pub", plaintext)

    my_utils.write_to_file('results_cipher_text_SimpleText.txt', ciphertext)

    resultPlainText = my_encryption.decrypt(keyLattice, ciphertext)

    my_utils.write_to_file('results_plain_text_SimpleText.txt', resultPlainText)

    pass


def encrypt_and_decrypt_LongWithKeywords():
    # read plain text
    plaintext = my_utils.read_to_end('data/LongTextWithKeywords.txt')
    keyLattice = 'long_text_key'
    N1 = NTRUdecrypt()
    N1.setNpq(N=167, p=3, q=128, df=61, dg=20, d=18)

    # Actually generate and save the public and private keys
    N1.genPubPriv(keyLattice)

    # debug
    N2 = NTRUdecrypt()
    N2.readPriv(keyLattice + ".priv")

    ciphertext = my_encryption.encrypt(keyLattice + ".pub", plaintext)

    my_utils.write_to_file('results_cipher_text_LongTextWithKeywords.txt', ciphertext)

    resultPlainText = my_encryption.decrypt(keyLattice, ciphertext)

    my_utils.write_to_file('results_plain_text_LongTextWithKeywords.txt', resultPlainText)

    pass


def encrypt_and_decrypt_JapaneseArticle():
    plaintext = my_utils.read_to_end('data/JapaneseArticle.txt')
    keyLattice = 'jpn_article_key'
    N1 = NTRUdecrypt()
    N1.setNpq(N=167, p=3, q=128, df=61, dg=20, d=18)

    # Actually generate and save the public and private keys
    N1.genPubPriv(keyLattice)

    # debug
    N2 = NTRUdecrypt()
    N2.readPriv(keyLattice + ".priv")

    ciphertext = my_encryption.encrypt(keyLattice + ".pub", plaintext)

    my_utils.write_to_file('results_cipher_text_JapaneseArticle.txt', ciphertext)

    resultPlainText = my_encryption.decrypt(keyLattice, ciphertext)

    my_utils.write_to_file('results_plain_text_JapaneseArticle.txt', resultPlainText)

    pass


def test_cases():
    encrypt_and_decrypt_simple()
    encrypt_and_decrypt_LongWithKeywords()
    encrypt_and_decrypt_JapaneseArticle()
    pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("-e", "--encrypt", required=False,
                          help="encryption")
    parser.add_argument("-d", "--decript", required=False,
                          help="decryption")
    parser.add_argument("-f", "--filepath", required=False,
                          help="file path")
    parser.add_argument("-k", "--keyname", required=False,
                          help="key name")
    parser.add_argument("-o", "--output", required=False,
                          help="output file")
    parser.add_argument("-r", "--replace", required=False,
                          help="replace sensitive word")
    args = vars(parser.parse_args())

    no_parameters = True
    for key in args.keys():
        if args[key] is not None:
            no_parameters = False
            break

    if no_parameters:
        test_cases()
    else:
        encrypt()
        decrypt()
