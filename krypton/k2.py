# Welcome to Krypton!
#
# This game is intended to give hands on experience with cryptography
# and cryptanalysis.  The levels progress from classic ciphers, to modern,
# easy to harder.
#
# Although there are excellent public tools, like cryptool,to perform
# the simple analysis, we strongly encourage you to try and do these
# without them for now.  We will use them in later excercises.
#
# ** Please try these levels without cryptool first **
#
#
# The first level is easy.  The password for level 2 is in the file
# 'krypton2'.  It is 'encrypted' using a simple rotation called ROT13.
# It is also in non-standard ciphertext format.  When using alpha characters for
# cipher text it is normal to group the letters into 5 letter clusters,
# regardless of word boundaries.  This helps obfuscate any patterns.
#
# This file has kept the plain text word boundaries and carried them to
# the cipher text.
#
# Enjoy!
#STAY WITHIN THE BOUNDS OF 65 AND 122
encrypted_text = "YRIRY GJB CNFFJBEQ EBGGRA"
#store the text in a array without space so you dont have to deal with spaces
enc_array = encrypted_text.split(" ")
new_array = []
changed_array = []
print(encrypted_text[0])
print(ord(encrypted_text[0]))
for string in enc_array:
    new_string = ""
    for character in string:
            new_char = ord(character)
            new_array.append(new_char)
            new_char2 = ord(character) - 13
            changed_array.append(new_char2)
for string in enc_array:
    new_string = ""
    for character in string:
        newChr = ord(character) - 13
        if newChr < 65:
            
print("ORIGINAL")
print(new_array)
print("NEW")
print(changed_array)
