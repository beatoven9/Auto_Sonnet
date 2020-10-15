
import requests
from bs4 import BeautifulSoup

###     This works but it's a lot of branches for something very simple.


### This needs a way to handle words with endings/suffixes that reroute to the root
###     example: demanded, demands, demander reroute to 'demand' the verb
### 
### one possible fix: (potentially slow)
###     find the html that says the word we are looking for
###     subtract that string from the string we're searching for
###         first output those strings to console on a large text to see 
###         what all of the potential cases are
###         have those endings in a separate dictionary with a tuple as a value
###             the tuple will contain:
###                 the IPA for the final syllable and how it pertains to the root
###                 an int for the number of syllables to be added to the root


def set_IPA(site, word):
    
    page = requests.get(site + word)
    soup = BeautifulSoup(page.content, 'html.parser')
    IPA_text = soup.find(class_='pron-ipa-content css-cqidvf evh0tcl2').text
    return clean_up(IPA_text)


def clean_up(IPA_text):
    
    comma_index = IPA_text.find(",")
    if comma_index > 0:
        IPA_text = IPA_text[:comma_index]
    

    ### this is to catch the semicolon in the words 'an' and 'the'
    semi_colon_index = IPA_text.find(";")
    if semi_colon_index > 0:
        IPA_text = IPA_text[:semi_colon_index]

    ### this is to delete the word "stressed" from the word 'the'
    sub_string = 'stressed'
    IPA_text = IPA_text.replace(sub_string, '')

    return IPA_text.replace("/", "").strip()

