#!/usr/bin/env python

import IPA_query
import json_Dictionary

#To do:     make a dictionary of IPA vowels so that in the ending syllable, we can chop off the leading consonant(s).
#           put this in the set_ending_syll() function.


###         There is a bug in this for at least the words 'the' and 'an'. and maybe some other one syllable words that 
###             have pronunciations that vary depending on the context. I dont want to fix it with more if statements though :///


class Word:


    def __init__(self, word):
        self.word = word
        self.site = 'https://www.dictionary.com/browse/'
        self.IPA_string = IPA_query.set_IPA(self.site, self.word)
        self.syll_array = self.set_syll_array()
        self.syllable_count = self.set_syll_count()
        self.stressed_syll = self.set_stressed_syll()
        self.secondary_stress = self.set_secondary_stress()
        self.ending_syll = self.set_ending_syll()
        self.dict = self.make_dict()
        self.info = self.get_info()
        

    def set_syll_array(self):
        apost_ind = self.IPA_string.find("ˈ")
        if apost_ind > 0 and self.IPA_string[apost_ind] != ' ':
            self.IPA_string = self.IPA_string[:apost_ind] + ' ' + self.IPA_string[apost_ind:]
        comma_ind = self.IPA_string.find("ˌ")
        if comma_ind > 0 and self.IPA_string[comma_ind] != ' ':
            self.IPA_string = self.IPA_string[:comma_ind] + ' ' + self.IPA_string[comma_ind:]
        return self.IPA_string.split(" ")


    def set_syll_count(self):
        return self.IPA_string.count(" ") + 1
               

    def set_stressed_syll(self):
        for i in range(len(self.syll_array)): 
            for char in self.syll_array[i]:
                if char == "ˈ":
                    return i


    def set_secondary_stress(self):
        for i in range(len(self.syll_array)): 
            for char in self.syll_array[i]:
                if char == "ˌ":
                    return i 

        
    def set_ending_syll(self):
        return self.syll_array[-1] 


    def get_info(self):
        formatted_info =  self.word + "\n\tIPA: " + self.IPA_string + "\n\tSyllable count: " + str(self.syllable_count) + "\n\tStressed Syllable Index: " + str(self.stressed_syll) + "\n\tSecondary Stress index: " + str(self.secondary_stress) + "\n\tEnding Syllable IPA: " + self.ending_syll
        return formatted_info


    def make_dict(self):
        word_dict = {
            "IPA": self.IPA_string,
            "syllable_count": self.syllable_count,
            "stressed_syllable": self.stressed_syll,
            "secondary_stress": self.secondary_stress,
            "ending_syllable": self.ending_syll
                    }
        return word_dict
                

    def send_to_json(self):
        Encode_Dictionary.dump_dict(self.dict)



