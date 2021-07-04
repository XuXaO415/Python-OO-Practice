"""Word Finder: finds random words from a dictionary."""
import random 

class WordFinder:
    """ Random word generator from a list of words
    >>> wf = WordFinder("/Users/student/words.txt")
3 words read

>>> wf.random()
'cat'

>>> wf.random()
'cat'

>>> wf.random()
'porcupine'

>>> wf.random()
'dog'

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
https://docs.python.org/3/tutorial/inputoutput.html

f = open('words.txt', 'r')
print(f.read())

f = open('smLst.txt', 'r')
print(f.read())


"""

    def __init__(self, f):
        """Reads from a small list of words from path"""
        f = open('smLst')
        print(f.read())
        
    def random(self):
        """Return a random word from smLst """
        return random.choice(self.smLst)
    
    
        
class SpecialWordFinder(WordFinder):