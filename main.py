#!/usr/bin/env python
from Word import Word
import json_Dictionary
import sys
import text_parser

###     Text comes in. each new word is added to a list.  
###     Json dictionary is read into another python dictionary.
###     Each word in the python dictionary is checked for existence in the json/python dictionary
###     If the word exists, no action is taken.
###     If the word does NOT exist, the word is looked up and then its dictionary representation is added to the 
###         json/python dictionary. 
###     The sonnet logic happens.
###     When the program is closed, the json/python dictionary is encoded back to pure json once more.


if __name__ == "__main__":
   
    json_file = 'dictionary.json'

    dict_data = json_Dictionary.decode_dict(json_file)
        

#    for arg in sys.argv[1:]:
#        if arg in dict_data.keys():
#            print("word: " + arg + " exists in dictionary\n")
#        else:
#            print("that word is not in the dictionary\n")
#            dict_data[arg] = Word(arg).dict
#    
    
    file_name = 'word.txt'

    word_list = text_parser.parse_text(file_name)
    
    for word in word_list:
        if word in dict_data.keys():
            print("word: " + word + " exists in dictionary\n")
        else:
            print("that word is not in the dictionary\n")
            dict_data[word] = Word(word).dict

    json_Dictionary.encode_dict(dict_data, json_file)

