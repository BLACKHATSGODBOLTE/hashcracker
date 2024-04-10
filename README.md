# Password Hash Cracker

This is a simple Python script for cracking hashed passwords using various hashing algorithms.

## Requirements
- Python 3.x
- requests
- hashlib
- bcrypt
- binascii

## Usage for Linux
1. Clone this repository or download the script file.
2. Install the required libraries if you haven't already using pip install -r requirements.txt.
3. Run the script by executing python hasher.py

## Usage for windows
1. Download the zip file of this repo
2. Run the hasher.exe file
3. Insert the hash type and wordlist path
4. See the cracking

## Features
- Supports cracking passwords hashed using MD5, SHA-1, BCRYPT, and CRC32 algorithms.
- Utilizes various hashing techniques for password cracking.
- Provides a visual animation during the cracking process.

## How to Use
1. When prompted, select the hash type you want to crack:
    - 1: MD5
    - 2: SHA-1
    - 3: BCRYPT
    - 4: CRC32
2. Enter the hash you want to crack.
3. Provide the filename containing the list of passwords to attempt.
4. The script will attempt to crack the provided hash using the selected hash type and display the result and also it will save the result in a txt file named "result".

## Note
- This script is for educational purposes only. Make sure you have the legal right to crack passwords before using it.

## Disclaimer
The authors of this script are not responsible for any misuse or illegal activities performed with it. Use at your own risk.
