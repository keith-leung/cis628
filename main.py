import yaml
import argparse

def encrypt():
    pass

def decrypt():
    pass


def encrypt_and_decrypt_simple():


    pass


def encrypt_and_decrypt_LongWithKeywords():
    pass


def encrypt_and_decrypt_JapaneseArticle():
    pass


def test_cases():
    encrypt_and_decrypt_simple()
    encrypt_and_decrypt_LongWithKeywords()
    encrypt_and_decrypt_JapaneseArticle()
    pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.parse_args()
    no_parameters = False

    if no_parameters:
        test_cases()
    else:
        encrypt()
        decrypt()
