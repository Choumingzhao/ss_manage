"""This python3 script generate a random password from characters in [0-9a-zA-Z], the default lengh of the password is 10.
"""
import random
from string import digits, ascii_lowercase, ascii_uppercase

def generatepd(NUM = 10):
    return ''.join([random.choice(digits + ascii_lowercase + ascii_uppercase) for i in range(NUM)])

if __name__ == "__main__":
    for i in range(10):
        print(generatepd(10))