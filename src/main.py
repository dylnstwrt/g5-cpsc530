#!/usr/bin/python3
import csv
import math
import random
import sys
# pip
import tqdm
from zxcvbn import zxcvbn
# local
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
            raw_password = random_lines.strip("\n")
            #omit passwords less than 4 characters long.
            if len(raw_password) < 4:
                continue
            passwords.append(raw_password)
            # print(random_lines)
        except Exception:
            continue
    return passwords


def brute_attempts(password) -> int:
    '''
    method:
        calculates number of brute attempts;

    parameters:
        password : string
            password to be analyzed.
    '''
    # 94 characters = printable ascii characters minus space
    # 94^3 removes the number of passwords with 3 characters (min length = 4)
    # rock you precludes a time before LUDS; therefore is it not seen
    return (pow(94, len(password)) - pow(94, 3))

    # TODO password strength entropy using brute guesses vs. zxcvbn guesses
    '''
        - frequence of patterns
        - number of patterns in a password
            - histogram of password patterns
        - password guesses
            - brute force
        - password entropy
            - nist (luds)
            - zxcvbn
        - most commmon warnings/feedback
        - write to file
            - determine formatting
    '''
def bit_entropy(attempts) -> int:
    '''
    method:
        calculates entropy using attempts required to guess password

    parameters:
        attempts : int
            number of attempts
    '''
    return math.log2(attempts)

def main():
    pattern_freqs = dict()  # keep track of unique patterns for summary
    pass_length_freqs = dict()  # for histogram of password lengths
    warning_freqs = dict()
    passwords = generate_passlist(10000)

    for password in tqdm.tqdm(passwords):
        try:
            pass_length_freqs[len(password)] = pass_length_freqs.get(len(password), 0) + 1
            results = zxcvbn(password)  # dict
            
            feedback = results.get("feedback")
            warning = feedback.get("warning")
            warning_freqs[warning] = warning_freqs.get(warning, 0) + 1

            sequence = results.get("sequence")  # list of dicts
            pattern_count = len(sequence)

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
