#!/usr/bin/env python


### This needs a way to handle punctuation.


def parse_text(file):
    text = open(file, "r")
    word_list = []

    for line in text.readlines():
        for word in line.split():
            if word not in word_list:
                word_list.append(word)


    return word_list


