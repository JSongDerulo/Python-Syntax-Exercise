def print_upper_words(words):
    """ prints each word from a list in a separate line in upper case """

    for word in words:
        print(word.upper())



def print_upper_words2(words):
    """ prints each word that starts with the letter "E" from a list in a separate line in upper case """

    for word in words:
        if word.upper().startswith("E"):
            print(word.upper())




def print_upper_words3(words, must_start_with):
    """ prings words that start with letters assigned by user 'must_start_with' and lists in a separate line in upper case """

    for word in words:
        for letter in must_start_with:
            if word.startswith(letter):
                print(word.upper())