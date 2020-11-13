#!/usr/bin/python3
import csv
import math
import random
import sys
#pip
import tqdm
from zxcvbn import zxcvbn
#local
from nist import nist_entropy

FILENAME = "./resources/rockyou.txt"


def generate_passlist(size) -> list:
    '''
    method:
        generates a list of passwords by randomly selecting a number of passwords
        based on params from a password file.

    parameters:
        size : int
            number of passwords to select from file.
    '''
    passwords = list()
    file = open(FILENAME, encoding="ISO-8859-1")
    lines = file.readlines()
    for i in tqdm.trange(size):
        try:
            random_lines = random.choice(lines)
            passwords.append(random_lines.strip("\n"))
            # print(random_lines)
        except Exception:
            continue
    return passwords


def brute_attempts(password) -> int:
    '''
    method:
        calculates number of brute attempts;
        TODO take into account LUDS requirements, and length requirements (total - bad_passwords)

    parameters:
        password : string
            password to be analyzed.
    '''
    #TODO deal with case sensitivity
    return (pow(69, len(password)))

    #TODO password strength entropy using brute guesses vs. zxcvbn guesses
    '''

    stats:
        - frequence of pattern
        - number of patterns in a password
            - histogram of password patterns
        - password guesses
            - brute force
        - password entropy
            - nist (luds)
                - informational vs. strength
            - zxcvbn
        - most commmon warnings/feedback
    '''
def main():
    pattern_freqs = dict()  # keep track of unique patterns for summary
    passwords = generate_passlist(10000)

    for password in tqdm.tqdm(passwords):
        try:
            results = zxcvbn(password)  # dict
            # TODO refactor into separate method.
            sequence = results.get("sequence")  # list of dicts
            # number of patterns =
            for pattern in sequence:
                pattern_name = pattern.get("pattern")
                if pattern_name == "dictionary":
                    pattern_name += "-"+pattern.get("dictionary_name")
                    if (pattern.get("l33t")):
                        pattern_name += "-l33t"
                    if (pattern.get("reversed")):
                        pattern_name += "-reversed"
                pattern_freqs[pattern_name] = pattern_freqs.get(
                    pattern_name, 0) + 1  # update frequency dict
        except Exception:
            continue


if __name__ == "__main__":
    main()
