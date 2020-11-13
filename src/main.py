import csv
import math
from random import random
from tqdm import tqdm
from zxcvbn import zxcvbn
from nist import nist_entropy


def main():
    errCount = 0
    with open("./resources/rockyou.txt", "r", encoding="ISO-8859-1") as file:
        for password in tqdm(file):
            try:
                #artifact with encoding
                password = password.strip('\n')
                # assumes no space in special character set; thus 33 special, 10 digit, and 26 alphabetical
                brute_attempts = (pow(69, len(password)))

                results = zxcvbn(password) # dict
                sequences = results.get("sequence") # list of dicts

                for sequence in sequences:
                    pattern = sequence.get("pattern")
                    if (sequence.get("l33t")): pattern += "-l33t"
                    if (sequence.get("reversed")): pattern += "-reversed"
                    print(pattern)
            except Exception:
                errCount += 1
                continue

if __name__ == "__main__":
    main()
 