__author__ = "Paul Grochocinski"
__copyright__ = "Copyright (C) 2013 Paul Grochocinski"
__licence__ = "Public Domain"
__version__ = "1.0"

import random

def create_keyfile(start=34, stop=127, filename=None):
    '''(int, int, str) -> None
    
       Create a secret key. If filename is specified, write the key to the
       named file.
       
       This is provided in case you want to generate new keys.
    '''
    from_list = list(range(start, stop))
    random.shuffle(from_list)
    group_length = random.randint(2,30)
    result = str(group_length) + '\n'
    for coding_char, cipher_char in zip(range(start, stop), from_list):
        result = result + (chr(coding_char) + chr(cipher_char)) + '\n'
    if filename != None:
        file = open(filename, 'w')
        file.write(result)
        file.close()
    else:
        print(result)


def encipher(plaintext, group_length, coding_char_to_ciphered_char):
    '''(str, int, dict of str to str) -> str

    Return a string that has been converted using coding_char_to_ciphered_char
    from plaintext and has been reversed.

    >>>encipher('a', 5, coding_char_to_ciphered_char):
    '|,nxs'
    
    '''

    # Create an empty str for enciphered text.
    enciphered_text = ''

    # Add 'STOP' to the end of plaintext.
    plaintext = plaintext + 'STOP'

    # Calculate whether plaintext is a multiple of group_length.
    extra_padding = len(plaintext) % group_length

    if extra_padding != 0:
        # If the remainder is not 0, add ' ' as many times to plaintext to
        # make the remainder 0. 
        plaintext = plaintext + (' ' * (group_length - extra_padding))

    # Reverse the plaintext in groups of group_length
    plaintext = reverse_message(plaintext, group_length)
        
    for char in plaintext:
        if char in coding_char_to_ciphered_char:
            # Convert the character from plaintext into its coded character.
            enciphered_text = enciphered_text +\
                              coding_char_to_ciphered_char[char]
        else:
            enciphered_text = enciphered_text + char

    return enciphered_text


def decipher(ciphertext, group_length, coding_char_to_ciphered_char):
    '''(str, int, dict of str to str) -> str

    Return a string that has been converted using coding_char_to_ciphered_char
    from ciphertext.

    >>>decipher('|,nxs', 5, coding_char_to_ciphered_char):
    'a'
    
    '''

    # Create an empty dictionary for the opposite conversion.
    decoding_char = {}

    for (old_key, old_value) in coding_char_to_ciphered_char.items():
        # Makes the old_value to be the new key and the old_key the new_value.
        decoding_char[old_value] = old_key

    # Create an empty str for deciphered text.
    deciphered_text = ''
    
    for char in ciphertext:
        if char in decoding_char:
            # Convert the character from the ciphertext into its
            # uncoded character.
            deciphered_text = deciphered_text + decoding_char[char]
        else:
            deciphered_text = deciphered_text + char

    # Reverse the deciphered text in groups of group_length, strip off
    # the trailing white space and remove the 'STOP'.
    final_text = reverse_message(deciphered_text, group_length).strip()[:-4]

    return final_text
    

def reverse_message(text, group_length):
    ''' (str, int) -> str

    Return a string that has reversed groups of group_length of some text.

    >>> reverse_message(['abcdef'])
    'cbafed'

    '''

    # Create an empty list.
    w = []

    # Create an empty str.
    message = ''

    for idx in range(0, len(text), group_length):
        # Create a list of group_length.
        group = list(text[idx : idx + group_length])
        group.reverse()
        w = w + group

    for char in w:
        # Add each character from the list w to the str.
        message = message + char

    return message


def reverse_groups(list_of_groups):
    '''(list of [list of str]) -> str
    
       Return a string that contains the reversed groups of some text.
       The original lists must remain unmodified.
       
       >>> reverse_groups([['A', 'B', 'C'], ['D', 'E', 'F']])
       'CBAFED'
       
    '''

    # Create an empty list for q.
    q = []

    # Create an empty str for the reveresed str.
    reversed_str = ''

    for lst in list_of_groups:
        # Reverse the list lst.
        lst.reverse()
        q = q + lst
        
    for char in q:
        # Add each character from the reversed list q to the str.
        reversed_str = reversed_str + str(char)   
    
    return reversed_str
    
    
def get_key(file):
    '''(file open for reading) -> tuple of objects
    
       Return a tuple containing an int of the group length and a dictionary
       of mapping pairs.

       >>>get_key('sample.key')
       (22, {'a': '3', 'b': 's'})
    '''

    # Create a dictionary for the cipher.
    coding_char_to_ciphered_char = {}

    # Assign the group length from the key to a variable.
    group_length = int(file.readline())

    for char in file:
        # Assign a key and its value from the key into the dictionary.
        coding_char_to_ciphered_char[char[0]] = char[1]
        
    return (group_length, coding_char_to_ciphered_char)


def get_key_file():
    '''() -> file open for reading
    
       Return the key file.
    '''

    # Prompt the user for the key file where the cipher is located.
    return open(input("Enter the name of the key file: "), 'r')


def get_text_filename():
    '''() -> str
    
       Return the name of the file containing the plaintext or cipher text.
    '''

    # Prompt the user for the text file where either the ciphered or
    # plaintext is located.
    return input("Enter the file to read: ")


def process(filename, group_length, coding_char_to_ciphered_char):
    ''' (file open for reading, int, dict) -> str or None
        
       If the filename provided ends in '.txt', encipher its contents and
       store the results in a new file with the same name, except with
       '.txt' replaced with '.enc'. If the filename does not end in '.txt',
       decipher the file's contents and print it to the screen.

       >>> process('sample.txt', 22, {a:d, f:d, h:i})
       None
       >>> process('sample.enc', 22, {a:d, f:d, h:i})
       'afh'
    '''

    # Open the text file that the user inputted.
    open_text = open(filename, 'r')

    # Read all the lines in the text.
    texts = open_text.readlines()

    # Create an empty str for the text.
    text = ''

    for line in texts:
        # Create a str with all the lines in text into 1 line.
        text = text + line

    # If the filename has an extension '.txt' execute below.
    if filename[-3:] == 'txt':
        # Use encipher function to encipher the text.
        final = encipher(text, group_length, coding_char_to_ciphered_char)

        # Create a new file using the same name as the text file
        # but with '.enc' extension.
        output = open(filename[:-3] + 'enc', 'w')

        # Write the enciphered text in the new file created.
        output.write(final)
    else:
        # Decipher the enciphered text using the decipher function.
        final = decipher(text, group_length, coding_char_to_ciphered_char)

        # Print the deciphered text to the screen.
        print(final)

    open_text.close()

    return
    

if __name__ == '__main__':
    # Read a keyfile.
    (group_length, coding_char_to_ciphered_char) = get_key(get_key_file())
    # Encipher/decipher a file using the key data obtained from the keyfile.
    process(get_text_filename(), group_length, coding_char_to_ciphered_char)
