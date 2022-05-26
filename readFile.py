# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

from types import NoneType


def read_file_content(filename):
    # [assignment] Add your code here 
    filename = open('story.txt', 'r')
    read_file = filename.read().replace('\n','').replace('?','')
    print(read_file)
    filename.close()
    return read_file


def count_words():
    text = read_file_content('story.txt')
    # [assignment] Add your code here
    my_dict = dict()
    
    words = text.strip().lower().split(" ")
    for word in words: 
     
      my_dict[word] = my_dict.get(word,0)+1
   
    return my_dict
print(count_words())