# PROFESSIONAL PORTFOLIO PROJECT
# PROJECT NAME - Text to Morse Code Converter
# PROJECT FUNCTIONALITY - A text-based Python program to convert Strings into Morse Code (and vice versa).

# NOTES
# For better readability, in conversion of strings to morse codes:
# i. a space is used to separate letter codes.
# ii. 3 spaces are used to separate word codes.


morse_dictionary = {
    "A": ".-", "B": "-...",
    "C": "-.-.", "D": "-..", "E": ".",
    "F": "..-.", "G": "--.", "H": "....",
    "I": "..", "J": ".---", "K": "-.-",
    "L": ".-..", "M": "--", "N": "-.",
    "O": "---", "P": ".--.", "Q": "--.-",
    "R": ".-.", "S": "...", "T": "-",
    "U": "..-", "V": "...-", "W": ".--",
    "X": "-..-", "Y": "-.--", "Z": "--..",
    "1": ".----", "2": "..---",
    "3": "...--", "4": "....-",
    "5": ".....", "6": "-.....",
    "7": "--...", "8": "---..",
    "9": "----.", "0": "-----",
    ",": "--..--",
    ".": ".-.-.-",
    "?": "..--..",
    "/": "-..-.",
    "'": ".----.",
    "!": "-.-.--",
    "-": "-....-",
    "(": "-.--.",
    ")": "-.--.-",
    "&": ".-...",
    ":": "---...",
    ";": "-.-.-.",
    "=": "-...-",
    "+": ".-.-.",
    "_": "..--.-",
    '"': '.-..-.',
    "$": "...-..-",
    "@": ".--.-."
    }


def text_to_morse_code(t_input):
    """Takes an input string containing punctuation mark(s) and/or alphanumeric character(s) and converts it to Morse code"""
    mc_statement = ""
    words_list = t_input.split(" ")
    for word in words_list:
        mc_word = ""
        for letter in word:
            if letter.upper() in morse_dictionary:
                mc_word += morse_dictionary[letter.upper()] + " "       # -->  see 'i.' under NOTES above
            else:
                print(f'ERROR. The character "{letter}" cannot be converted to a morse code as it does not have a code entry.')
                print("Conversion Process Aborted!")
                return
        mc_word = mc_word.rstrip()            # -->  removes the trailing space from the morse code of the last letter
        mc_statement += mc_word + "   "       # -->  see 'ii.' under NOTES above
    output_morse_code = mc_statement.rstrip()
    print()
    print(f'The Input statement is "{t_input}"')
    print(f'Its morse code equivalent is "{output_morse_code}"')


def morse_code_to_text(mc_input):
    """Takes an input morse code and converts it to a string containing punctuation mark(s) and/or alphanumeric character(s)"""
    text_statement = ""
    mc_words_list = mc_input.split("   ")
    for mc_word in mc_words_list:
        word = ""
        mc_letters_list = mc_word.split(" ")
        for mc_letter in mc_letters_list:
            for char in morse_dictionary:
                if mc_letter == morse_dictionary[char]:
                    word += char
        text_statement += word + " "
    output_text_statement = text_statement.strip()
    print()
    print(f'The input morse code is "{mc_input}"')
    print(f'Its language meaning is "{output_text_statement}"')


print("\n****** WELCOME TO THE TEXT TO MORSE CODE CONVERTER *****\n")

print("Choose the type of conversion you want to perform...")
print()

valid_entry = False
while not valid_entry:
    conversion_type = input("Enter 1 for Text to Morse Code, OR 2 for Morse Code to Text: ")
    if conversion_type in ["1", "2"]:
        valid_entry = True
        if conversion_type == "1":
            text_input = input("Please type in the text you want to convert to morse code: ")
            text_to_morse_code(t_input=text_input)
        else:
            morse_code_input = input("Please select the morse code you want to convert to text: ")
            morse_code_to_text(mc_input=morse_code_input)
    else:
        print(f"ERROR. The entered key '{conversion_type}' is invalid. Please make a valid selection.")
    print()
