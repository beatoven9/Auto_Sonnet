#!/usr/bin/env python
from IPA import IPA
import sys

if __name__ == "__main__":
    for arg in sys.argv[1:]:
        word = IPA(arg)
        print(word.info)

