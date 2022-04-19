import pandas as pd
import numpy as np
from textblob import TextBlob
import re

def build_classifier():
    return None

def choose_pattern():
    return 0

def parse(entry, key):
    pattern = None
    if key == 0:
        pattern = re.compile("To [a-zA-Z]* \[([a-zA-Z]*)\](\D*)for ([a-zA-Z]*) for ([0-9]) ([a-zA-Z]*) value \([(0-9)]\)")
        match = pattern.match(entry)
        out = str(match.group(4)) + ',,,' + str(match.group(5)) + ',,'
        return out
    # pattern that involves [To] NAME INT..INT..[INT] (with possibility of no brackets and single/two names)
    if key == 1:
        pattern = re.compile("[To] ([a-zA-Z])* ([0-9])..([0-9])..\[*([0-9])\]*")
        match = pattern.match(entry)
        out = ''''''
        

def __main__():
    return

if __name__ == '__main__':
    __main__()