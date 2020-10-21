# Auto_Sonnet

nonfunctional work in progress at the moment

### notes to myself....

json dictionary is populated by a webscrape of dictionary.com/ that functionality is still not all there yet. I'm running into some issues with inconsistent html
class names for the IPA of seemingly random words. It should be an easy fix whenever I get around to it. there seems only to be a few different forms of the html
so a little bit of exception handling should do the trick.

I will probably have the json dict populate a list of 5-6k common words. 

it will probably help keep the size smaller to save the infinitives of each verb only and then perhaps the language of origin or some other information which will 
inform another program how to conjugate the verb. this would give access to all verb forms without having to save each one in the dictionary. this verb conjugator 
will probably be my next endeavor.

eventually i planned to have the json dictionary map to a python dictionary of rhymes based on the last syllable of the word's IPA and a python dictionary of 
words with syllable lengths as the keys after that, the logic for writing which words are able to precede which words will be simple. I'm not sure how i'll work out 
grammar... maybe I'll use an external library for that, at least for the short term.
