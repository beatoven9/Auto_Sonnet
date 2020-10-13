#!/usr/bin/env python
from Word import Word
import sys

if __name__ == "__main__":
    for arg in sys.argv[1:]:
        new_word = Word(arg)
        print(new_word.info)

