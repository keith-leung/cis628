# CIS 628 Lattice-based Encryption with Chinese Characters and Anti-Sensitive Word Recognition

# Introduction
This repository creates an application that combines the lattice-based encryption algorithm and a customized Vigenère cipher algorithm and use this algorithm to protect the network writer from content leak. Lattice-based encryption, which is considered to be safe in quantum computing era, is used to encrypt the key and code table that are used by the customized Vigenère cipher, which can only contain common characters without messy code. Using this encryption can make the encrypted article version-tracking friendly, so that the cloud storage can store the text version changes, which provide a revision history for the writer. 

# Getting Started
## Prerequisite
1.	Python 3.8 or higher version
2.	pip 22 or higher version

## Required packages
please install the packages with
```shell
pip install -r requirements.txt
```
requirements.txt resides in the working directory

## Project Structure
### Metadata 
Folder data contains:
* the whole CJK character dataset 
* sensitive keyword dataset [Sensitive_***.txt]
### NTRU
An implementation of lattice-based encryption
### Configuration file
config.yaml, which is a yaml configuration file, contains metadata lists. Adding or removing items in the lists can change the metadata. 

# Run and Test
**CAUTION: Lattice-based encryption/decryption takes a long-running time (10+ minutes for encryption, 16+ minutes for decryption) on every file, please be patient.**
Or you can remove the test case from the config.yaml file, then the related test cases will skip. 
## Run with command line
First, please clone or download the project.
Then: 
```shell
python main.py
```
## Debug Mode
Due to the long-running time of Lattice-based encryption/decryption by NTRU, setting the code to debug mode can skip the lattice-based encryption, which can save a lot of testing time.
In the configuration file **config.yaml**, set the global config item **IsDebug: True** can skip the Lattice-based encryption/decryption.

## Test cases
### Run all embedded test cases
The embedded test cases are: 
* Simple Text Encryption and Decryption
* Long Text Encryption and Decryption
* Japanese Article Encryption and Decryption
```shell
python main.py
```
**Due to very limited development time, this project only provides a very limited option to run, which is run all embedded test cases.**
But changing the files:
* LongTextWithKeywords.txt
* JapaneseArticle.txt
* SimpleText.txt

in data/ folder can make the program run with different articles. 

# Acknowledgement
Many thanks NTRU_Python https://github.com/pointedsphere/NTRU_python
