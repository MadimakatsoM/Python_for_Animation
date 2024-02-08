import re
from collections import Counter


# a regex pattern is used as a sequence of characters that define a search pattern
# the join (as the name indicates) join these strings, inserting a | between them 

def split(delimiters, text):
    regex_pattern = '|'.join(map(re.escape, delimiters))
    return re.split(regex_pattern, text, 0)

#Returns all the words in a sentance as seperate elements in a list

def convert_to_word_list(text):
   
    text = filter(None, re.split(r'[,|;|?|. ]+', text))
    lowercase = list(map(str.lower,text))
    return lowercase

#Prints words longer than specified length

def words_longer_than(length, text):
    
    words = convert_to_word_list(text)
    result = [word for word in words if len(word) > length]
    return result
    
if __name__ == "__main__":
    text = 'Today I had an amazing session with my colleagues , at work .How about you?'
    length = 10
    delimiters = ',|;|?|.|' '|'
    
    print(convert_to_word_list(text))
    
    print(words_longer_than(length,text))
    
    