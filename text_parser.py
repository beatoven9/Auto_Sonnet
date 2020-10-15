#!/usr/bin/env python
import string


def parse_text(file):
    text = open(file, "r")
    word_list = []

    for line in text.readlines():
        for word in line.split():
            word = word.translate(str.maketrans('', '', string.punctuation)).lower()
            if word not in word_list:
                word_list.append(word)


    return word_list


