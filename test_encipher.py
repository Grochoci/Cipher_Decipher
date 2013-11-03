import a2
import unittest

dictionary = {'>': 'N', '<': '+', ':': '[', '8': '8', '6': 'R', 
              '4': '2', '2': ']', '0': 'f', '.': 'd', ',': 'Y', 
              '*': 'K', '(': '=', '&': '{', '$': '4', '"': 'I', 
              '^': 'e', '\\': 'P', 'Z': '"', 'X': 'j', 'V': 'r',
              'T': 'n', 'R': 'k', 'P': '|', 'N': "'", 'L': 'O', 
              'J': '*', 'H': '1', 'F': 'U', 'D': '9', 'B': '}', 
              '@': '@', '~': 'X', '|': 'F', 'z': '5', 'x': 'Q', 
              'v': ':', 't': '`', 'r': 'c', 'p': ';', 'n': 'v', 
              'l': 'Z', 'j': 'm', 'h': 'E', 'f': 'V', 'd': 'g', 
              'b': 'S', '`': '?', '?': 'u', '=': 'w', ';': 'B', 
              '9': '%', '7': '$', '5': '>', '3': '0', '1': 'b', 
              '/': 'q', '-': 'W', '+': 'o', ')': 'M', "'": 'H', 
              '%': 'C', '#': '^', '_': '&', ']': 'y', '[': '/', 
              'Y': 'h', 'W': '#', 'U': '_', 'S': 'x', 'Q': 'i', 
              'O': ',', 'M': 'T', 'K': 'l', 'I': 'A', 'G': '<', 
              'E': '7', 'C': 'G', 'A': ')', '}': 'z', '{': '3', 
              'y': '~', 'w': 'D', 'u': 'J', 's': '.', 'q': '-', 
              'o': '\\', 'm': 'a', 'k': 'L', 'i': 't', 'g': 'p',
              'e': '6', 'c': '(', 'a': 's'}

class TestEncipher(unittest.TestCase):

    def test_empty(self):
        ''' Testing with empty plaintext.'''

        assert a2.encipher('', 5, dictionary) == ' |,nx', 'Empty str failed'

    def test_one_alpha(self):
        ''' Testing with one alpha character and length = group_length'''

        assert a2.encipher('a', 5, dictionary) == '|,nxs', 'One alpha str failed'

    def test_multiple_alpha(self):
        ''' Testing with multiple alpha characters and length != group_length'''

        assert a2.encipher('abc', 5, dictionary) == 'nx(Ss   |,', 'Multiple alpha str failed'

    def test_upper_alpha(self):
        ''' Testing with one upper alpha character.'''

        assert a2.encipher('A', 5, dictionary) == '|,nx)', 'One upper alpha str failed'

    def test_multiple_upper_alpha(self):
        ''' Testing with multiple upper alpha characters.'''

        assert a2.encipher('ABC', 5, dictionary) == 'nxG})   |,', 'Multiple upper alpha str failed'

    def test_mix_alpha(self):
        ''' Testing with mix of upper and lower alpha characters.'''

        assert a2.encipher('aBcD', 5, dictionary) == 'x9(}s  |,n', 'Mix of upper and lower alpha str failed'

    def test_number(self):
        ''' Testing with number as str.'''

        assert a2.encipher('3', 5, dictionary) == '|,nx0', 'One number as str failed'

    def test_numbers(self):
        ''' Testing with numbers as str.'''

        assert a2.encipher('456', 5, dictionary) == 'nxR>2   |,', 'Multiple numbers as str failed'

    def test_punctuation(self):
        ''' Testing with punctuation.'''

        assert a2.encipher('%', 5, dictionary) == '|,nxC', 'Punctuation failed'

    def test_multiple_punctuations(self):
        ''' Testing with multiple punctuations.'''

        assert a2.encipher('&?"', 5, dictionary) == 'nxIu{   |,', 'Multiple punctuations failed'
        
    def test_numbers_alpha_puntc(self):
        ''' Testing with upper and lower alpha, punctuations and numbers as str.'''

        assert a2.encipher('aB1?', 5, dictionary) == 'xub}s  |,n', 'Mix of upper, lower alpha, punctuations, and numbers as str failed'

    def test_space(self):
        ''' Testing with space in str.'''

        assert a2.encipher('Hi Jonathan', 5, dictionary) == '\\* t1sE`sv|,nxv', 'Str with space in the middle failed'

    def test_new_line(self):
        ''' Testing with muliple lines in file.'''

        assert a2.encipher('New\nLine', 5, dictionary) == "O\nD6'nx6vt   |,", 'Str with multiple lines failed'


    def test_stop_in_str(self):
        ''' Testing with STOP in str to be enciphered.'''

        assert a2.encipher('STOP', 5, dictionary) == 'x|,nx  |,n', 'Str with STOP in plaintext'
        
unittest.main(exit = False)
