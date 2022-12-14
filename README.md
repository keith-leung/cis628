# CIS 628 Lattice-based Encryption with Chinese Characters and Anti-Sensitive Word Recognition

# Introduction
This repository creates an application that combines the lattice-based encryption algorithm and a customized Vigenère cipher algorithm and use this algorithm to protect the network writer from content leak. Lattice-based encryption, which is considered to be safe in quantum computing era, is used to encrypt the key and code table that are used by the customized Vigenère cipher, which can only contain common characters without messy code. Using this encryption can make the encrypted article version-tracking friendly, so that the cloud storage can store the text version changes, which provide a revision history for the writer. 

# Getting Started
## Prerequisite
1.	Python 3.8 or higher version
2.	pip 22 or higher version

## Required packages
please install the packages with
```
pip -r requirements.txt
```
requirements.txt resides in the working directory

# Run and Test
## Run with command line
```
```


## Test cases

### Simple Text encryption and decryption

### Long Text encryption and decryption

# Acknowledgement
Many thanks NTRU_Python https://github.com/pointedsphere/NTRU_python
