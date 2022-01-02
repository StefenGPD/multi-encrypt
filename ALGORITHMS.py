# Import random for the key maker
import random

# List of letters to be used in each cipher #
alphabet = ['P', 'j', '|', 'p', 'T', '=', 'u', '8', 'W', 'U', '6', 'O', 'V', ':', 'I', 'F',
                '\\', '[', '(', 'b', '3', 'K', 'L', '{', 'w', '&', 'l', '0', 'd', 'n', 'a', ')',
                'S', 'C', '@', 'm', '?', '%', 'N', 'o', 'c', 'D', 'A', ';', '#', 'H', 'R', '1',
                'z', 'f', 'M', 'e', "'", 'i', 'X', '"', '>', 'G', 'x', 'y', '-', 'J', '5', 'k',
                '.', 's', '!', '2', 'Z', ',', '_', 'q', 't', '*', 'h', '^', '$', '9', '7', '+',
                'r', '}', 'B', 'Y', '4', '/', 'E', 'g', 'v', 'Q', '<', ']', ' ']

# --------- CIPHERS --------- #
#
# CAESAR CIPHER
#   activity:   either "encryption" or "decryption"
#   text:       string of text
#   value:      integer
#   function:   shifts to the right
#
# MOD CAESAR CIPHER
#   activity:   either "encryption" or "decryption"
#   text:       string of text
#   valueList:  list containing integers
#   function:   shifts to the right, traversing through list
#               will loop through until end of string of text
#
# ALTERNATIVE / ALTERNATING CIPHER
#   activity:   either "encryption" or "decryption"
#   text:       string of text
#   valueList:  list containing 2 integers
#   function:   shift left with 1st integer then shift right with 2nd integer and so on and so forth
#
# VIGENERE CIPHER
#   activity:       either "encryption" or "decryption"
#   text:           string of text
#   valueString:    string of text
#   function:       use index of each letter in alphabet to caesar cipher the corresponding letter.
#                   Will loop through until end of string of text.
#   NOTE: Since it's a string, check the index of it's character sa alphabet list, start index will be 0
#


def caesar(activity, text, value=0):
    if activity == "encryption":
        value = value
        #LOL same lang
    elif activity == "decryption":
        value = -value
    ciphertext = ""
    for letter in text:
        if letter in alphabet:
            letterpos = alphabet.index(letter)
            shifted = alphabet[(alphabet.index(letter) + value) % len(alphabet)]
            ciphertext += shifted
        else:
            ciphertext += " "
    return ciphertext


def mod_caesar(activity, text, valuelist):
    if activity == "decryption":
        decryptionValues = []
        for i in valuelist:
            decryptionValues.append(i*-1)
        valuelist = decryptionValues
    ciphertext = ""
    key_counter = len(valuelist)
    for letter in text:
        list_number = valuelist[key_counter % len(valuelist)]
        ciphertext += caesar("encryption", letter, list_number)
        key_counter += 1
    return ciphertext


def alternating_caesar(activity, text, valuelist=[0, 0]):
    if activity == "decryption":
        decryptionValues = []
        for i in valuelist:
            decryptionValues.append(i*-1)
        valuelist = decryptionValues

    ciphertext = ""
    counter = 0

    for letter in text:
        if letter in alphabet:
            letterpos = alphabet.index(letter)
            if counter % 2 == 0:
                value = -(valuelist[0])
            else:
                value = valuelist[1]
            counter += 1
            shifted = alphabet[(alphabet.index(letter) + value) % len(alphabet)]
            ciphertext += shifted
        else:
            ciphertext += " "
    return ciphertext


def vigenere(activity, message, valueString):

    # This is like the setup part of Vigenere's algorithm

    # Raven's algorithm used a string of characters for his alphabet so it
    # will just turn the alphabet list into a concatenated string

    strAlphabet = ""

    for character in alphabet:
        strAlphabet += character

    letter_to_index = dict(zip(strAlphabet, range(len(strAlphabet))))
    index_to_letter = dict(zip(range(len(strAlphabet)), strAlphabet))

    # This is like the end of setup part of Vigenere's algorithm

    if activity == "encryption":
        sign = 1
    elif activity == "decryption":
        sign = -1
    else:
        sign = None

    ciphertext = ""
    split_message = [
        message[i : i + len(valueString)] for i in range(0, len(message), len(valueString))
    ]

    for each_split in split_message:
        i = 0
        for letter in each_split:
            number = (letter_to_index[letter] + (sign * (letter_to_index[valueString[i]]))) % len(strAlphabet)
            ciphertext += index_to_letter[number]
            i += 1

    return ciphertext


# The modes are: caesar, vigenere, modified, alternating
def make_key(mode=None):
    # CODE FOR CAESAR KEY
    if mode == "caesar":
        # Pos/neg determines whether the value will be positive or negative
        pos_neg = random.randrange(-1, 2, 2)
        key = random.randint(1, len(alphabet) - 1) * pos_neg


    # CODE FOR VIGENERE KEY
    elif mode == "vigenere":
        key = ""
        key_length = random.randint(2, len(alphabet))
        # Populating the key with random values
        for i in range(key_length):
            key += alphabet[random.randint(0, len(alphabet) - 1)]


    # CODE FOR MODIFIED CAESAR KEY
    elif mode == "modified":
        key = list()
        key_length = random.randint(2, len(alphabet))
        # Populating the key with random values
        for i in range(key_length):
            pos_neg = random.randrange(-1, 2, 2)
            key.append(random.randint(1, len(alphabet) - 1) * pos_neg)

    # CODE FOR ALTERNATING CAESAR KEY
    elif mode == "alternating":
        key = list()
        key_length = 2
        # Populating the key with random values
        for i in range(key_length):
            pos_neg = random.randrange(-1, 2, 2)
            key.append(random.randint(1, len(alphabet) - 1) * pos_neg)


    else:
        print("Mode is undefined, please try again.")
        return None

    return key

# MAKING OF THE KEYS #
def make_key_list():
    key = make_key("caesar")
    keyListModified = make_key("modified")
    keyListAlternating = make_key("alternating")
    keyString = make_key("vigenere")

    return [key, keyListModified, keyListAlternating, keyString]

# MESSAGE TO BE ENCRYPTED #
message = "THIS IS A LONG STRING FOR TESTING OUR ENCRYPTION AND DECRYPTION"

# ENCRYPTION #
#
#   caesarMessageEncryption = caesar("encryption", message, key)
#   modifiedCaesarMessageEncryption = mod_caesar("encryption", caesarMessageEncryption, keyListModified)
#   alternatingCaesarMessageEncryption = alternating_caesar("encryption", modifiedCaesarMessageEncryption, keyListAlternating)
#   vigenereMessageEncryption = vigenere("encryption", alternatingCaesarMessageEncryption, keyString)
#
# ENCRYPTION #

# PLACE KEYS TO VARIABLE #
# PINASOK LANG YUNG ENCRYPTION SA TAAS SA LOOB NG ISA'T ISA #

finalKey = make_key_list()

def auf_encrypt(finalKey, message):
    return vigenere("encryption", alternating_caesar("encryption", mod_caesar("encryption", caesar("encryption", message, finalKey[0]), finalKey[1]), finalKey[2]), finalKey[3])

encryptedMessage = auf_encrypt(finalKey, message)

# DECRYPTION #
#
#   vigenereMessageDecryption = vigenere("decryption", encryptedMessage, finalKey[-1])
#   alternatingCaesarMessageDecryption = alternating_caesar("decryption", vigenereMessageDecryption, finalKey[-2])
#   modifiedCaesarMessageDecryption = mod_caesar("decryption", alternatingCaesarMessageDecryption, finalKey[-3])
#   caesarMessageDecryption = caesar("decryption", modifiedCaesarMessageDecryption, finalKey[-4])
#
# DECRYPTION #

# PINASOK LANG YUNG DECRYPTION SA TAAS SA LOOB NG ISA'T ISA #

def auf_decrypt(finalKey, encryptedMessage):
    return caesar("decryption", mod_caesar("decryption", alternating_caesar("decryption", vigenere("decryption", encryptedMessage, finalKey[-1]), finalKey[-2]), finalKey[-3]), finalKey[-4])

decryptedMessage = auf_decrypt(finalKey, encryptedMessage)

print("ORIGINAL MESSAGE IS: " + message)
print()

print("ENCRYPTED WITH MULTI LAYER ENCRYPTION: " + encryptedMessage)
print("KEY: " + str(finalKey))
print()

print("DECRYPTED WITH MULTI LAYER DECRYPTION: " + decryptedMessage)